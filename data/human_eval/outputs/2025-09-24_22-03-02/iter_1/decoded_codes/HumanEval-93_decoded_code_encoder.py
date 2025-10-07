def encode(msg):
    vowels = "aeiouAEIOU"
    repl = {v: chr(ord(v) + 2) for v in vowels}
    msg = msg.swapcase()
    return "".join([repl[c] if c in repl else c for c in msg])