def digits(pq: int) -> int:
    yz: int = 1
    gm: int = 0
    s: str = str(pq)
    for index in range(1, len(s)):
        hx: int = int(s[index])
        if hx % 2 == 0:
            break
        else:
            yz *= hx
            gm += 1
            break
    if gm == 0:
        return 0
    return yz