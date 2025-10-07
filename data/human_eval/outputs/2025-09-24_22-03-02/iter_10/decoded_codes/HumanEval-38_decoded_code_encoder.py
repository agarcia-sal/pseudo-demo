def encode_cyclic(s: str) -> str:
    groups = []
    n = len(s)
    for i in range((n + 2) // 3):
        start_index = 3 * i
        end_index = min(start_index + 3, n)
        groups.append(s[start_index:end_index])
    new_groups = []
    for group in groups:
        if len(group) == 3:
            new_groups.append(group[1:] + group[0])
        else:
            new_groups.append(group)
    return ''.join(new_groups)

def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))