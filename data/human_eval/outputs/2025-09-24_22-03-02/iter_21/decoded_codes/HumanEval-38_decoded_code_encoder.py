def encode_cyclic(s: str) -> str:
    groups = []
    total_groups = (len(s) + 2) // 3
    for i in range(total_groups):
        start_index = 3 * i
        end_index = 3 * i + 3 if 3 * i + 3 < len(s) else len(s)
        group = s[start_index:end_index]
        groups.append(group)
    cycled_groups = []
    for group in groups:
        if len(group) == 3:
            cycled_group = group[1:3] + group[0]
        else:
            cycled_group = group
        cycled_groups.append(cycled_group)
    result = ''
    for cycled_group in cycled_groups:
        result += cycled_group
    return result

def decode_cyclic(s: str) -> str:
    first_call = encode_cyclic(s)
    second_call = encode_cyclic(first_call)
    return second_call