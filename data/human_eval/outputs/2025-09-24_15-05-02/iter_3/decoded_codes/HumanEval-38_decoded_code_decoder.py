def encode_cyclic(s: str) -> str:
    groups = []
    n = len(s)
    # Split s into groups of 3 characters
    for i in range((n + 2) // 3):
        start_index = 3 * i
        end_index = min(3 * i + 3, n)
        group = s[start_index:end_index]
        groups.append(group)

    # Rotate each full-length group by moving first char to the end
    for i in range(len(groups)):
        group = groups[i]
        if len(group) == 3:
            groups[i] = group[1:] + group[0]

    return ''.join(groups)


def decode_cyclic(s: str) -> str:
    # Decoding is done by applying encode_cyclic twice
    return encode_cyclic(encode_cyclic(s))