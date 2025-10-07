def encode_cyclic(s: str) -> str:
    groups = []
    number_of_groups = (len(s) + 2) // 3
    for i in range(number_of_groups):
        start_index = 3 * i
        end_index = min(3 * i + 3, len(s))
        groups.append(s[start_index:end_index])

    for i, group in enumerate(groups):
        if len(group) == 3:
            groups[i] = group[1:] + group[0]

    return "".join(groups)


def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))