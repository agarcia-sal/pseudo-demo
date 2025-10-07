def encode_cyclic(s: str) -> str:
    groups = []
    length_s = len(s)
    count_groups = (length_s + 2) // 3
    for i in range(count_groups):
        start_index = 3 * i
        end_index = start_index + 3
        if end_index > length_s:
            end_index = length_s
        group = s[start_index:end_index]
        groups.append(group)
    cycled_groups = []
    for j in range(len(groups)):
        group = groups[j]
        if len(group) == 3:
            cycled_group = group[1:3] + group[0]
            cycled_groups.append(cycled_group)
        else:
            cycled_groups.append(group)
    result = ""
    for k in range(len(cycled_groups)):
        result += cycled_groups[k]
    return result

def decode_cyclic(s: str) -> str:
    intermediate_result = encode_cyclic(s)
    final_result = encode_cyclic(intermediate_result)
    return final_result