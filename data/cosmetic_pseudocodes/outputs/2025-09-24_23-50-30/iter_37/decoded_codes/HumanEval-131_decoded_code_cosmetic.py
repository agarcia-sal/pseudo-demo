def digits(m: int) -> int:
    acc: int = 1
    cnt: int = 0
    for ch in str(m):
        val: int = int(ch)
        if val % 2 == 1:
            acc *= val
            cnt += 1
    return 0 if cnt == 0 else acc