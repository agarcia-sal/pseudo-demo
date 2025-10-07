def encode_cyclic(s: str) -> str:
    groups = []
    group_count = (len(s) + 2) // 3
    for i in range(group_count):
        start_index = 3 * i
        end_index = min(3 * i + 3, len(s))
        groups.append(s[start_index:end_index])

    for index in range(len(groups)):
        group = groups[index]
        if len(group) == 3:
            groups[index] = group[1:] + group[0]

    return ''.join(groups)

def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))