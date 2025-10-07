def encode_cyclic(s: str) -> str:
    groups = [s[i*3 : min(i*3 + 3, len(s))] for i in range((len(s) + 2) // 3)]
    cycled_groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    return ''.join(cycled_groups)

def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))