def encode_cyclic(s: str) -> str:
    groups = []
    length_of_s = len(s)
    number_of_groups = (length_of_s + 2) // 3
    for i in range(number_of_groups):
        start_index = 3 * i
        if (3 * i + 3) <= length_of_s:
            end_index = 3 * i + 3
        else:
            end_index = length_of_s
        substring = s[start_index:end_index]
        groups.append(substring)
    cycled_groups = []
    for j in range(len(groups)):
        group = groups[j]
        length_of_group = len(group)
        if length_of_group == 3:
            cycled_group = group[1:3] + group[0]
        else:
            cycled_group = group
        cycled_groups.append(cycled_group)
    result_string = ""
    for k in range(len(cycled_groups)):
        result_string += cycled_groups[k]
    return result_string

def decode_cyclic(s: str) -> str:
    first_call_result = encode_cyclic(s)
    second_call_result = encode_cyclic(first_call_result)
    return second_call_result