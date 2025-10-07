def encode_cyclic(s: str) -> str:
    groups = []
    total_groups = (len(s) + 2) // 3
    for i in range(total_groups):
        start_index = 3 * i
        end_index = min(3 * i + 3, len(s))
        group = s[start_index:end_index]
        groups.append(group)
    for index in range(len(groups)):
        group = groups[index]
        if len(group) == 3:
            groups[index] = group[1:] + group[0]
        else:
            groups[index] = group
    result = ''.join(groups)
    return result

def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))