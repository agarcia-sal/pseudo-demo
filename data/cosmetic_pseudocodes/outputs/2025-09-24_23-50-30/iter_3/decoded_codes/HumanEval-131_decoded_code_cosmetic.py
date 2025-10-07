def digits(n: int) -> int:
    prod: int = 1
    count_odds: int = 0
    s: str = str(n)
    for i in range(len(s)):
        d: str = s[i]
        val: int = int(d)
        if val % 2 != 0:
            prod *= val
            count_odds += 1
    return 0 if count_odds == 0 else prod