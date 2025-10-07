def encode_cyclic(s: str) -> str:
    groups = []
    length_s = len(s)
    number_of_groups = (length_s + 2) // 3
    for i in range(number_of_groups):
        start_index = 3 * i
        end_index = start_index + 3
        if end_index > length_s:
            end_index = length_s
        substring = ""
        for j in range(start_index, end_index):
            substring += s[j]
        groups.append(substring)
    new_groups = []
    for k in range(len(groups)):
        group = groups[k]
        group_length = len(group)
        if group_length == 3:
            cycled_group = ""
            for m in range(1, 3):
                cycled_group += group[m]
            cycled_group += group[0]
            new_groups.append(cycled_group)
        else:
            new_groups.append(group)
    result = ""
    for n in range(len(new_groups)):
        result += new_groups[n]
    return result

def decode_cyclic(s: str) -> str:
    first_call_result = encode_cyclic(s)
    second_call_result = encode_cyclic(first_call_result)
    return second_call_result