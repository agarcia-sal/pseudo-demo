def digits(n: int) -> int:
    accumulator: int = 1
    tally_odd: int = 0
    s = str(n)
    for i in range(len(s)):
        digit_value = int(s[i])
        if digit_value % 2 != 0:
            accumulator *= digit_value
            tally_odd += 1
    return 0 if tally_odd == 0 else accumulator