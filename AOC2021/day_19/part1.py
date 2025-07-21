from itertools import groupby, combinations, permutations, product
import math

class Scanner:
    """
    Represents a single scanner and its detected beacons. 
    Responsible for parsing input and computing beacon distance signatures.
    """
    def __init__(self, scanned_values, num):
        self.scanner_num = num
        self.beacons = list(self.__parse_input_data__(scanned_values))
        self._beacon_pairs_ = [list(comb) for comb in combinations(self.beacons, 2)]
    
    def __parse_input_data__(self, group_data):
        for coords in group_data:
            yield [int(x) for x in coords.split(',')]
    
    def calculate_distances(self):
        """Calculates all pairwise distances between beacons. Used for quick overlap checks."""
        self.distances = {(tuple(start), tuple(end)): math.dist(start, end) for start, end in self._beacon_pairs_}
        self.beacons_per_distance = {k: v for v, k in self.distances.items()}

    def check_distances_with_other_scanner(self, other_scanner):
        """
        Quickly checks for a minimum overlap in distance fingerprints between this scanner and another.
        Returns the list of shared distances if enough overlap is found.
        """
        this_scanner_distances = set(self.distances.values())
        other_scanner_distances = set(other_scanner.distances.values())
        common_part = this_scanner_distances & other_scanner_distances
        if len(common_part) >= 12 * 11 / 2:
            return list(common_part)
        return None

class ScannerAlignment:
    """
    Stores a possible alignment (rotation + translation) between two scanners.
    Can apply and invert transformations.
    """
    def __init__(self, scanner_a, scanner_b, same_distances):
        self.scanner_a = scanner_a
        self.scanner_b = scanner_b
        self.same_distances = same_distances
        self.scanner_numbers = (scanner_a.scanner_num, scanner_b.scanner_num)
        self.aligned = False

    @staticmethod
    def all_rotations():
        """Yields all 24 possible axis permutations and sign flips (true 3D orientations)."""
        perms = list(permutations([0, 1, 2]))
        signs = list(product([1, -1], repeat=3))
        for perm in perms:
            for sign in signs:
                yield perm, sign

    def find_alignment(self):
        """
        Brute-forces all rotations and translations to align at least 12 beacons with the reference scanner.
        Stores the first valid transformation found.
        """
        a_points = set(tuple(b) for b in self.scanner_a.beacons)
        for perm, sign in self.all_rotations():
            b_rotated = [[sign[i]*b[perm[i]] for i in range(3)] for b in self.scanner_b.beacons]
            for pt_a in self.scanner_a.beacons:
                for pt_b in b_rotated:
                    offset = [pt_a[i] - pt_b[i] for i in range(3)]
                    transformed = [tuple(pt[i] + offset[i] for i in range(3)) for pt in b_rotated]
                    matches = sum(t in a_points for t in transformed)
                    if matches >= 12:
                        self.perm = perm
                        self.sign = sign
                        self.offset = offset
                        self.aligned = True
                        return
        self.aligned = False

    def rotate_point(self, p):
        """Applies the stored rotation (perm + sign flip) to a single point."""
        return [self.sign[i] * p[self.perm[i]] for i in range(3)]

    def invert(self):
        """
        Computes the inverse transformation for aligning in the opposite direction.
        Used when attaching a scanner via a reversed edge in the alignment graph.
        """
        inv_perm = [0, 0, 0]
        inv_sign = [0, 0, 0]
        for i, p in enumerate(self.perm):
            inv_perm[p] = i
            inv_sign[p] = self.sign[i]
        def inv_rot(pt):
            return [inv_sign[i] * pt[inv_perm[i]] for i in range(3)]
        inv_offset = [-x for x in inv_rot(self.offset)]
        return inv_rot, inv_offset

class ScannerMap:
    """
    Incrementally builds the global map by anchoring scanners one by one using valid alignments.
    Transforms all detected beacons into the global coordinate system.
    """
    def __init__(self, scanners, scanner_alignments):
        self.scanners = scanners
        self.alignments = scanner_alignments
        self.N = len(scanners)
        self.poses = {0: (lambda p: p, [0, 0, 0])}
        self.global_beacons = set(tuple(b) for b in scanners[0].beacons)
        self._build_map()

    def _build_map(self):
        """
        Anchors all scanners using discovered alignments, supporting both alignment directions.
        Each new scanner has its rotation and offset composed with the global map so far.
        """
        anchored = set([0])
        to_anchor = set(range(1, self.N))
        while to_anchor:
            progress = False
            for alignment in self.alignments:
                a, b = alignment.scanner_numbers
                # Forward direction: attach b to anchored a
                if a in anchored and b in to_anchor and alignment.aligned:
                    rot_a, off_a = self.poses[a]
                    def composed_rot(pt, alignment=alignment, rot_a=rot_a):
                        return rot_a(alignment.rotate_point(pt))
                    new_offset = [off_a[i] + rot_a(alignment.offset)[i] for i in range(3)]
                    self.poses[b] = (composed_rot, new_offset)
                    for pt in self.scanners[b].beacons:
                        gpt = tuple(composed_rot(pt)[i] + new_offset[i] for i in range(3))
                        self.global_beacons.add(gpt)
                    anchored.add(b)
                    to_anchor.remove(b)
                    progress = True
                    break
                # Reverse direction: attach a to anchored b via the inverted transformation
                if b in anchored and a in to_anchor and alignment.aligned:
                    rot_b, off_b = self.poses[b]
                    inv_rot, inv_offset = alignment.invert()
                    def composed_rot(pt, inv_rot=inv_rot, rot_b=rot_b):
                        return rot_b(inv_rot(pt))
                    new_offset = [off_b[i] + rot_b(inv_offset)[i] for i in range(3)]
                    self.poses[a] = (composed_rot, new_offset)
                    for pt in self.scanners[a].beacons:
                        gpt = tuple(composed_rot(pt)[i] + new_offset[i] for i in range(3))
                        self.global_beacons.add(gpt)
                    anchored.add(a)
                    to_anchor.remove(a)
                    progress = True
                    break
            if not progress:
                print("Unable to anchor all scanners. Remaining:", to_anchor)
                break

    def count_beacons(self):
        """Returns the number of unique beacons in the global map."""
        return len(self.global_beacons)

with open('input.txt') as file:
    inputs = [line.strip() for line in file if not line.startswith('--')]
    groups = [list(group) for k, group in groupby(inputs, key=bool) if k]

scanners = [Scanner(group, num) for num, group in enumerate(groups)]

for scanner in scanners:
    scanner.calculate_distances()

scanner_alignments = []
for scanner_a, scanner_b in list(combinations(scanners, 2)):
    same_distances = scanner_a.check_distances_with_other_scanner(scanner_b)
    if same_distances is not None:
        align = ScannerAlignment(scanner_a, scanner_b, same_distances)
        align.find_alignment()
        if align.aligned:
            scanner_alignments.append(align)

global_map = ScannerMap(scanners, scanner_alignments)
print("Number of unique beacons:", global_map.count_beacons())