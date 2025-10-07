def encode_cyclic(s):
    gs = [s[3*i : 3*i+3] for i in range((len(s) + 2) // 3)]
    gs = [(g[1:] + g[0]) if len(g) == 3 else g for g in gs]
    return ''.join(gs)

def decode_cyclic(s):
    return encode_cyclic(encode_cyclic(s))