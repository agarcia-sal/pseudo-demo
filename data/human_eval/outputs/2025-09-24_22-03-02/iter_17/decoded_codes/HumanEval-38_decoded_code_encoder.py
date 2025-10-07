def encode_cyclic(s: str) -> str:
    groups = []
    count = (len(s) + 2) // 3
    for i in range(count):
        start_index = 3 * i
        end_index = 3 * i + 3 if 3 * i + 3 < len(s) else len(s)
        substring = s[start_index:end_index]
        groups.append(substring)
    new_groups = []
    for group in groups:
        if len(group) == 3:
            cycled_group = group[1:] + group[0]
            new_groups.append(cycled_group)
        else:
            new_groups.append(group)
    result = ''.join(new_groups)
    return result

def decode_cyclic(s: str) -> str:
    first_call = encode_cyclic(s)
    second_call = encode_cyclic(first_call)
    return second_call