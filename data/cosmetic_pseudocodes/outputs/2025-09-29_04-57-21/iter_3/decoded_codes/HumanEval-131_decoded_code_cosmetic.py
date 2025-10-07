def digits(n: int) -> int:
    accum: int = 1
    num_odds: int = 0
    s = str(n)
    for idx in range(len(s)):
        val = int(s[idx])
        if val % 2 != 0:
            accum *= val
            num_odds += 1
    if num_odds == 0:
        return 0
    return accum