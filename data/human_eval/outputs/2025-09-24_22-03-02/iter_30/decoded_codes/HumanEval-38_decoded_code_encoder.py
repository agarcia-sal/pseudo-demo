def encode_cyclic(s: str) -> str:
    groups = []
    length_s = len(s)
    count_groups = (length_s + 2) // 3
    index_i = 0
    while index_i < count_groups:
        start_index = 3 * index_i
        end_index_candidate = 3 * index_i + 3
        end_index = length_s if end_index_candidate > length_s else end_index_candidate
        substring = s[start_index:end_index]
        groups.append(substring)
        index_i += 1
    new_groups = []
    index_j = 0
    count_groups = len(groups)
    while index_j < count_groups:
        group = groups[index_j]
        length_group = len(group)
        if length_group == 3:
            first_char = group[0]
            rest_chars = group[1:3]
            rotated_group = rest_chars + first_char
            new_groups.append(rotated_group)
        else:
            new_groups.append(group)
        index_j += 1
    result = ""
    index_k = 0
    count_new_groups = len(new_groups)
    while index_k < count_new_groups:
        current_group = new_groups[index_k]
        result += current_group
        index_k += 1
    return result


def decode_cyclic(s: str) -> str:
    intermediate = encode_cyclic(s)
    result = encode_cyclic(intermediate)
    return result