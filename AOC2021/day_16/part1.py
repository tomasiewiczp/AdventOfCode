def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return read_hook.readline()

def hex_to_bin(hexstr):
    return ''.join(bin(int(c, 16))[2:].zfill(4) for c in hexstr.strip())

def parse_packet(binstr, pos=0):
    version = int(binstr[pos:pos+3], 2)
    type_id = int(binstr[pos+3:pos+6], 2)
    pos += 6
    version_sum = version

    if type_id == 4:
        # Literal value
        while True:
            group = binstr[pos:pos+5]
            pos += 5
            if group[0] == "0":
                break
        return version_sum, pos

    # Operator
    length_type_id = binstr[pos]
    pos += 1
    if length_type_id == "0":
        total_len = int(binstr[pos:pos+15], 2)
        pos += 15
        subpacket_end = pos + total_len
        while pos < subpacket_end:
            v_sum, new_pos = parse_packet(binstr, pos)
            version_sum += v_sum
            pos = new_pos
        return version_sum, pos
    else:
        num_subpackets = int(binstr[pos:pos+11], 2)
        pos += 11
        for _ in range(num_subpackets):
            v_sum, new_pos = parse_packet(binstr, pos)
            version_sum += v_sum
            pos = new_pos
        return version_sum, pos

mapping_string = '0123456789ABCDEF'
input = read_input_file('input.txt')
binstr = ''.join([format(mapping_string.index(l),'04b') for l in input])
version_sum, _ = parse_packet(binstr)
print(version_sum)