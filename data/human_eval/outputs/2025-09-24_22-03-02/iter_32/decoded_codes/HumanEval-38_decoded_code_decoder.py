def encode_cyclic(s: str) -> str:
    groups = []
    length_s = len(s)
    count = (length_s + 2) // 3
    i = 0
    while i < count:
        start_index = 3 * i
        end_index_temp = 3 * i + 3
        if end_index_temp > length_s:
            end_index = length_s
        else:
            end_index = end_index_temp
        group = s[start_index:end_index]
        groups.append(group)
        i += 1
    new_groups = []
    j = 0
    groups_length = len(groups)
    while j < groups_length:
        group_j = groups[j]
        group_length = len(group_j)
        if group_length == 3:
            part1 = group_j[1:3]
            part2 = group_j[0]
            new_group = part1 + part2
            new_groups.append(new_group)
        else:
            new_groups.append(group_j)
        j += 1
    result = ""
    k = 0
    new_groups_length = len(new_groups)
    while k < new_groups_length:
        result += new_groups[k]
        k += 1
    return result


def decode_cyclic(s: str) -> str:
    first_encode = encode_cyclic(s)
    second_encode = encode_cyclic(first_encode)
    return second_encode