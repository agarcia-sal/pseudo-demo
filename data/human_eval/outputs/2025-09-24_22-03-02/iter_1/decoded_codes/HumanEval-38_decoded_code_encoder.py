def encode_cyclic(s):
    G = [s[3*i : 3*i+3] for i in range(len(s)//3)]
    G = [g[1:] + g[0] if len(g) == 3 else g for g in G]
    return ''.join(G)

def decode_cyclic(s):
    return encode_cyclic(encode_cyclic(s))