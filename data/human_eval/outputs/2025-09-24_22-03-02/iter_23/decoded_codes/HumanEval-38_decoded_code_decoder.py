def encode_cyclic(s: str) -> str:
    groups = []
    length_s = len(s)
    num_groups = (length_s + 2) // 3
    for i in range(num_groups):
        start_index = 3 * i
        if 3 * i + 3 < length_s:
            end_index = 3 * i + 3
        else:
            end_index = length_s
        subgroup = s[start_index:end_index]
        groups.append(subgroup)
    cycled_groups = []
    for group in groups:
        if len(group) == 3:
            first_char = group[0:1]
            remaining_chars = group[1:3]
            cycled_group = remaining_chars + first_char
            cycled_groups.append(cycled_group)
        else:
            cycled_groups.append(group)
    result = ''
    for cycled_group in cycled_groups:
        result += cycled_group
    return result

def decode_cyclic(s: str) -> str:
    encoded_once = encode_cyclic(s)
    encoded_twice = encode_cyclic(encoded_once)
    return encoded_twice