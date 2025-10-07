def encode_cyclic(s: str) -> str:
    groups = []
    for i in range((len(s) + 2) // 3):
        start_index = 3 * i
        end_index = min(3 * i + 3, len(s))
        group = s[start_index:end_index]
        if len(group) == 3:
            group = group[1:] + group[0]
        groups.append(group)
    return ''.join(groups)

def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))