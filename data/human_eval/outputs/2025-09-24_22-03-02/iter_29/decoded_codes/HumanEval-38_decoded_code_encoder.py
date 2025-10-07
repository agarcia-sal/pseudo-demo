def encode_cyclic(s: str) -> str:
    groups = []
    groups_count = (len(s) + 2) // 3
    for i in range(groups_count):
        start_index = 3 * i
        end_index = len(s)
        if 3 * i + 3 < end_index:
            end_index = 3 * i + 3
        group = ''
        for j in range(start_index, end_index):
            group += s[j]
        groups.append(group)
    new_groups = []
    for k in range(len(groups)):
        group = groups[k]
        if len(group) == 3:
            cycled_group = ''
            for m in range(1, 3):
                cycled_group += group[m]
            cycled_group += group[0]
            new_groups.append(cycled_group)
        else:
            new_groups.append(group)
    result = ''
    for n in range(len(new_groups)):
        result += new_groups[n]
    return result

def decode_cyclic(s: str) -> str:
    first_call_result = encode_cyclic(s)
    second_call_result = encode_cyclic(first_call_result)
    return second_call_result