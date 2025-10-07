def encode_cyclic(s: str) -> str:
    groups = []
    length_s = len(s)
    count_groups = (length_s + 2) // 3
    i = 0
    while i < count_groups:
        start_index = 3 * i
        end_index_candidate = 3 * i + 3
        end_index = end_index_candidate if end_index_candidate <= length_s else length_s
        group = s[start_index:end_index]
        groups.append(group)
        i += 1
    new_groups = []
    j = 0
    while j < len(groups):
        group = groups[j]
        length_group = len(group)
        if length_group == 3:
            part1 = group[1:length_group]
            part2 = group[0:1]
            new_group = part1 + part2
        else:
            new_group = group
        new_groups.append(new_group)
        j += 1
    result = ""
    k = 0
    while k < len(new_groups):
        current_group = new_groups[k]
        result += current_group
        k += 1
    return result

def decode_cyclic(s: str) -> str:
    first_call = encode_cyclic(s)
    second_call = encode_cyclic(first_call)
    return second_call