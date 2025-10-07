def encode_cyclic(s: str) -> str:
    groups = []
    length_s = len(s)
    count_groups = (len(s) + 2) // 3
    for i in range(count_groups):
        start_index = 3 * i
        end_index = start_index + 3
        if end_index > length_s:
            end_index = length_s
        substring = s[start_index:end_index]
        groups.append(substring)
    cycled_groups = []
    for j in range(len(groups)):
        group = groups[j]
        if len(group) == 3:
            new_group = group[1:3] + group[0]
            cycled_groups.append(new_group)
        else:
            cycled_groups.append(group)
    result = ''
    for k in range(len(cycled_groups)):
        result += cycled_groups[k]
    return result

def decode_cyclic(s: str) -> str:
    first_call = encode_cyclic(s)
    second_call = encode_cyclic(first_call)
    return second_call