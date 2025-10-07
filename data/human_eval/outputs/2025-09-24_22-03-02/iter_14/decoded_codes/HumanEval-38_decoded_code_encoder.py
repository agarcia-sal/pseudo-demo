def encode_cyclic(s: str) -> str:
    groups = []
    total_groups = (len(s) + 2) // 3
    for i in range(total_groups):
        start_index = 3 * i
        end_index = min(3 * i + 3, len(s))
        group = s[start_index:end_index]
        groups.append(group)
    cycled_groups = []
    for group in groups:
        if len(group) == 3:
            cycled_group = group[1:3] + group[0:1]
            cycled_groups.append(cycled_group)
        else:
            cycled_groups.append(group)
    result = ''
    for element in cycled_groups:
        result += element
    return result

def decode_cyclic(s: str) -> str:
    once_encoded = encode_cyclic(s)
    twice_encoded = encode_cyclic(once_encoded)
    return twice_encoded