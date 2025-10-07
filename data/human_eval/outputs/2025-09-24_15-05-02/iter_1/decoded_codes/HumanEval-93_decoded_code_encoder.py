def encode(msg):
    v = "aeiouAEIOU"
    r = {c: chr(ord(c)+2) for c in v}
    return "".join(r[c] if c in r else c for c in msg.swapcase())