def encode_cyclic(s: str) -> str:
    groups = []
    for i in range((len(s) + 2) // 3):
        start_index = 3 * i
        end_index = min(3 * i + 3, len(s))
        groups.append(s[start_index:end_index])

    encoded_groups = []
    for group in groups:
        if len(group) == 3:
            encoded_groups.append(group[1:] + group[0])
        else:
            encoded_groups.append(group)

    return ''.join(encoded_groups)


def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))