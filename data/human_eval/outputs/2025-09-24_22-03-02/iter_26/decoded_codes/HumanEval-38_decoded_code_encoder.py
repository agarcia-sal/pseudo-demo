def encode_cyclic(s: str) -> str:
    groups = []
    input_length = len(s)
    number_of_groups = (input_length + 2) // 3
    for i in range(number_of_groups):
        start_index = 3 * i
        end_index = 3 * i + 3 if 3 * i + 3 <= input_length else input_length
        group = s[start_index:end_index]
        groups.append(group)
    new_groups = []
    for group in groups:
        if len(group) == 3:
            cycled_group = group[1:] + group[0]
            new_groups.append(cycled_group)
        else:
            new_groups.append(group)
    result_string = ''.join(new_groups)
    return result_string

def decode_cyclic(s: str) -> str:
    first_call_result = encode_cyclic(s)
    second_call_result = encode_cyclic(first_call_result)
    return second_call_result