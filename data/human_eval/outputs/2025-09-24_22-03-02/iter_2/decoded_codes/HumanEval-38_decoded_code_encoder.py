def encode_cyclic(s: str) -> str:
    groups = []
    count = (len(s) + 2) // 3
    for i in range(count):
        start_index = 3 * i
        end_index = min(3 * i + 3, len(s))
        group = s[start_index:end_index]
        groups.append(group)

    cycled_groups = []
    for group in groups:
        if len(group) == 3:
            cycled_group = group[1:] + group[0]
        else:
            cycled_group = group
        cycled_groups.append(cycled_group)

    return ''.join(cycled_groups)

def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))