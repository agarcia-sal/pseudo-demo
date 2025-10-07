def digits(x: int) -> int:
    acc: int = 1
    tally: int = 0
    for symbol in str(x):
        val: int = int(symbol)
        if val % 2 != 0:
            acc *= val
            tally += 1
    return 0 if tally == 0 else acc