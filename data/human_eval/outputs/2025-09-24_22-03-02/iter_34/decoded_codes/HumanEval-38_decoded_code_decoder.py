def encode_cyclic(s: str) -> str:
    groups = []
    length_s = len(s)
    number_of_groups = (length_s + 2) // 3
    for i in range(number_of_groups):
        start_index = 3 * i
        end_index_candidate = start_index + 3
        end_index = end_index_candidate if end_index_candidate <= length_s else length_s
        substring = s[start_index:end_index]
        groups.append(substring)
    new_groups = []
    for group in groups:
        group_length = len(group)
        if group_length == 3:
            cycled_group = group[1:] + group[0]
            new_groups.append(cycled_group)
        else:
            new_groups.append(group)
    result = ''.join(new_groups)
    return result

def decode_cyclic(s: str) -> str:
    first_encoding = encode_cyclic(s)
    second_encoding = encode_cyclic(first_encoding)
    return second_encoding