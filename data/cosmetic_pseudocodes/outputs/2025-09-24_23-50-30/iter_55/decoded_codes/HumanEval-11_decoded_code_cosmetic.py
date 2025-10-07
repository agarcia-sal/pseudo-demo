def string_xor(w1: str, w2: str) -> str:
    def inner_xor(c1: str, c2: str) -> str:
        # Return '0' if characters are equal, else '1'
        return '0' if c1 == c2 else '1'

    acc: str = ""
    idx: int = 0

    while idx < len(w1):
        acc += inner_xor(w1[idx], w2[idx])
        idx += 1

    return acc