def encrypt(s: str) -> str:
    d = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(d[(d.index(c) + 4) % 26] if c in d else c for c in s)