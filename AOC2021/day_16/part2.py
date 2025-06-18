def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return read_hook.readline().strip()

def hex_to_bin(hexstr):
    return ''.join(bin(int(c, 16))[2:].zfill(4) for c in hexstr.strip())

def parse_packet(binstr, pos=0):
    version = int(binstr[pos:pos+3], 2)
    type_id = int(binstr[pos+3:pos+6], 2)
    pos += 6

    if type_id == 4:
        # Literal value
        literal_bin = ''
        while True:
            group = binstr[pos:pos+5]
            literal_bin += group[1:]
            pos += 5
            if group[0] == "0":
                break
        value = int(literal_bin, 2)
        return value, pos

    # Operator packet
    length_type_id = binstr[pos]
    pos += 1
    subpacket_values = []
    if length_type_id == "0":
        total_len = int(binstr[pos:pos+15], 2)
        pos += 15
        subpacket_end = pos + total_len
        while pos < subpacket_end:
            value, new_pos = parse_packet(binstr, pos)
            subpacket_values.append(value)
            pos = new_pos
    else:
        num_subpackets = int(binstr[pos:pos+11], 2)
        pos += 11
        for _ in range(num_subpackets):
            value, new_pos = parse_packet(binstr, pos)
            subpacket_values.append(value)
            pos = new_pos

    # Zwracanie wartości zależnie od type_id
    if type_id == 0:
        return sum(subpacket_values), pos
    elif type_id == 1:
        prod = 1
        for v in subpacket_values:
            prod *= v
        return prod, pos
    elif type_id == 2:
        return min(subpacket_values), pos
    elif type_id == 3:
        return max(subpacket_values), pos
    elif type_id == 5:
        return (1 if subpacket_values[0] > subpacket_values[1] else 0), pos
    elif type_id == 6:
        return (1 if subpacket_values[0] < subpacket_values[1] else 0), pos
    elif type_id == 7:
        return (1 if subpacket_values[0] == subpacket_values[1] else 0), pos
    else:
        raise ValueError(f"Unknown type_id: {type_id}")

input = read_input_file('input.txt')
binstr = hex_to_bin(input)
value, _ = parse_packet(binstr)
print(value)