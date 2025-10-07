def encode_cyclic(s: str) -> str:
    groups = []
    length_s = len(s)
    num_groups = (length_s + 2) // 3
    for i in range(num_groups):
        start_index = 3 * i
        end_index = start_index + 3
        if end_index > length_s:
            end_index = length_s
        group = s[start_index:end_index]
        groups.append(group)
    new_groups = []
    for group in groups:
        length_group = len(group)
        if length_group == 3:
            first_char = group[0]
            rest_chars = group[1:3]
            cycled_group = rest_chars + first_char
            new_groups.append(cycled_group)
        else:
            new_groups.append(group)
    result = ''.join(new_groups)
    return result

def decode_cyclic(s: str) -> str:
    first_encode = encode_cyclic(s)
    second_encode = encode_cyclic(first_encode)
    return second_encode