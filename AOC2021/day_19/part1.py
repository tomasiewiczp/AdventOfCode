from itertools import groupby, combinations, permutations, product
import math

class Scanner:
    """
    Represents a single scanner and its detected beacons.
    Responsible for parsing input and computing beacon distance signatures.
    """
    def __init__(self, scanned_values, scanner_id):
        self.scanner_id = scanner_id
        self.beacons = list(self._parse_input_data(scanned_values))
        self.beacon_pairs = [list(pair) for pair in combinations(self.beacons, 2)]
    
    def _parse_input_data(self, group_data):
        for coords in group_data:
            yield [int(x) for x in coords.split(',')]
    
    def calculate_distances(self):
        """Calculates all pairwise distances between beacons. Used for quick overlap checks."""
        self.distances = {(tuple(start), tuple(end)): math.dist(start, end) for start, end in self.beacon_pairs}
        self.beacons_per_distance = {key: value for value, key in self.distances.items()}

    def check_distances_with_other_scanner(self, other_scanner):
        """
        Quickly checks for a minimum overlap in distance fingerprints between this scanner and another.
        Returns the list of shared distances if enough overlap is found.
        """
        self_distances = set(self.distances.values())
        other_distances = set(other_scanner.distances.values())
        common_distances = self_distances & other_distances
        if len(common_distances) >= 12 * 11 / 2:
            return list(common_distances)
        return None

class ScannerAlignment:
    """
    Stores a possible alignment (rotation + translation) between two scanners.
    Can apply and invert transformations.
    """
    def __init__(self, reference_scanner, candidate_scanner, shared_distances):
        self.reference_scanner = reference_scanner
        self.candidate_scanner = candidate_scanner
        self.shared_distances = shared_distances
        self.scanner_pair = (reference_scanner.scanner_id, candidate_scanner.scanner_id)
        self.aligned = False

    @staticmethod
    def all_rotations():
        """Yields all 24 possible axis permutations and sign flips (true 3D orientations)."""
        for axes_order in permutations([0, 1, 2]):
            for axis_signs in product([1, -1], repeat=3):
                yield axes_order, axis_signs

    def find_alignment(self):
        """
        Brute-forces all rotations and translations to align at least 12 beacons with the reference scanner.
        Stores the first valid transformation found.
        """
        reference_points = set(tuple(beacon) for beacon in self.reference_scanner.beacons)
        for axes_order, axis_signs in self.all_rotations():
            rotated_candidate_beacons = [
                [axis_signs[index] * beacon[axes_order[index]] for index in range(3)]
                for beacon in self.candidate_scanner.beacons
            ]
            for reference_beacon in self.reference_scanner.beacons:
                for rotated_candidate_beacon in rotated_candidate_beacons:
                    translation_vector = [
                        reference_beacon[index] - rotated_candidate_beacon[index]
                        for index in range(3)
                    ]
                    transformed_beacons = [
                        tuple(rotated_beacon[index] + translation_vector[index] for index in range(3))
                        for rotated_beacon in rotated_candidate_beacons
                    ]
                    matching_beacons = sum(
                        transformed_beacon in reference_points for transformed_beacon in transformed_beacons
                    )
                    if matching_beacons >= 12:
                        self.axes_order = axes_order
                        self.axis_signs = axis_signs
                        self.translation_vector = translation_vector
                        self.aligned = True
                        return
        self.aligned = False

    def rotate_point(self, point):
        """Applies the stored rotation (axes_order + sign flip) to a single point."""
        return [self.axis_signs[index] * point[self.axes_order[index]] for index in range(3)]

    def invert(self):
        """
        Computes the inverse transformation for aligning in the opposite direction.
        Used when attaching a scanner via a reversed edge in the alignment graph.
        """
        inverse_axes_order = [0, 0, 0]
        inverse_axis_signs = [0, 0, 0]
        for index, axis in enumerate(self.axes_order):
            inverse_axes_order[axis] = index
            inverse_axis_signs[axis] = self.axis_signs[index]
        def inverse_rotate(point):
            return [inverse_axis_signs[index] * point[inverse_axes_order[index]] for index in range(3)]
        inverse_translation_vector = [-value for value in inverse_rotate(self.translation_vector)]
        return inverse_rotate, inverse_translation_vector

class ScannerMap:
    """
    Incrementally builds the global map by anchoring scanners one by one using valid alignments.
    Transforms all detected beacons into the global coordinate system.
    """
    def __init__(self, scanners, scanner_alignments):
        self.scanners = scanners
        self.alignments = scanner_alignments
        self.num_scanners = len(scanners)
        self.scanner_poses = {0: (lambda point: point, [0, 0, 0])}
        self.global_beacons = set(tuple(beacon) for beacon in scanners[0].beacons)
        self._build_map()

    def _build_map(self):
        """
        Anchors all scanners using discovered alignments, supporting both alignment directions.
        Each new scanner has its rotation and offset composed with the global map so far.
        """
        anchored_scanner_ids = set([0])
        unanchored_scanner_ids = set(range(1, self.num_scanners))
        while unanchored_scanner_ids:
            progress_made = False
            for alignment in self.alignments:
                reference_id, candidate_id = alignment.scanner_pair
                # Forward direction: attach candidate to anchored reference
                if reference_id in anchored_scanner_ids and candidate_id in unanchored_scanner_ids and alignment.aligned:
                    reference_rot, reference_offset = self.scanner_poses[reference_id]
                    def composed_rotation(point, alignment=alignment, reference_rot=reference_rot):
                        return reference_rot(alignment.rotate_point(point))
                    new_offset = [
                        reference_offset[index] + reference_rot(alignment.translation_vector)[index]
                        for index in range(3)
                    ]
                    self.scanner_poses[candidate_id] = (composed_rotation, new_offset)
                    for beacon in self.scanners[candidate_id].beacons:
                        global_beacon = tuple(
                            composed_rotation(beacon)[index] + new_offset[index] for index in range(3)
                        )
                        self.global_beacons.add(global_beacon)
                    anchored_scanner_ids.add(candidate_id)
                    unanchored_scanner_ids.remove(candidate_id)
                    progress_made = True
                    break
                # Reverse direction: attach reference to anchored candidate via the inverted transformation
                if candidate_id in anchored_scanner_ids and reference_id in unanchored_scanner_ids and alignment.aligned:
                    candidate_rot, candidate_offset = self.scanner_poses[candidate_id]
                    inverse_rotate, inverse_translation_vector = alignment.invert()
                    def composed_rotation(point, inverse_rotate=inverse_rotate, candidate_rot=candidate_rot):
                        return candidate_rot(inverse_rotate(point))
                    new_offset = [
                        candidate_offset[index] + candidate_rot(inverse_translation_vector)[index]
                        for index in range(3)
                    ]
                    self.scanner_poses[reference_id] = (composed_rotation, new_offset)
                    for beacon in self.scanners[reference_id].beacons:
                        global_beacon = tuple(
                            composed_rotation(beacon)[index] + new_offset[index] for index in range(3)
                        )
                        self.global_beacons.add(global_beacon)
                    anchored_scanner_ids.add(reference_id)
                    unanchored_scanner_ids.remove(reference_id)
                    progress_made = True
                    break
            if not progress_made:
                print("Unable to anchor all scanners. Remaining:", unanchored_scanner_ids)
                break

    def count_beacons(self):
        """Returns the number of unique beacons in the global map."""
        return len(self.global_beacons)

with open('input.txt') as file:
    input_lines = [line.strip() for line in file if not line.startswith('--')]
    scanner_groups = [list(group) for key, group in groupby(input_lines, key=bool) if key]

scanners = [Scanner(group, scanner_id) for scanner_id, group in enumerate(scanner_groups)]

for scanner in scanners:
    scanner.calculate_distances()

scanner_alignments = []
for reference_scanner, candidate_scanner in list(combinations(scanners, 2)):
    shared_distances = reference_scanner.check_distances_with_other_scanner(candidate_scanner)
    if shared_distances is not None:
        alignment = ScannerAlignment(reference_scanner, candidate_scanner, shared_distances)
        alignment.find_alignment()
        if alignment.aligned:
            scanner_alignments.append(alignment)

scanner_map = ScannerMap(scanners, scanner_alignments)
print("Number of unique beacons:", scanner_map.count_beacons())