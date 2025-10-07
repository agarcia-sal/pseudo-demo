def encode_cyclic(s: str) -> str:
    groups = []
    for index in range((len(s) + 2) // 3):
        start_index = index * 3
        end_index = min(start_index + 3, len(s))
        groups.append(s[start_index:end_index])

    cycled_groups = []
    for group in groups:
        if len(group) == 3:
            cycled_groups.append(group[1:] + group[0])
        else:
            cycled_groups.append(group)

    return ''.join(cycled_groups)

def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))