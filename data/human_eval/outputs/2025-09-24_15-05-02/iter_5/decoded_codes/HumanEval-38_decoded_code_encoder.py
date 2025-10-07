from math import ceil

def encode_cyclic(s: str) -> str:
    groups = []
    total_groups = ceil(len(s) / 3)
    for i in range(total_groups):
        group = s[3 * i : min(3 * i + 3, len(s))]
        groups.append(group)
    cycled_groups = []
    for group in groups:
        if len(group) == 3:
            cycled_groups.append(group[1:] + group[0])
        else:
            cycled_groups.append(group)
    encoded_string = "".join(cycled_groups)
    return encoded_string

def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))