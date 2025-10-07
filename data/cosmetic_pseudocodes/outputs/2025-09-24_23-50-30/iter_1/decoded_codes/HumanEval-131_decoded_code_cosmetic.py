def digits(n: int) -> int:
    product = 1
    odd_count = 0
    s = str(n)
    for i in range(len(s)):
        digit = int(s[i])
        if digit % 2 != 0:
            product *= digit
            odd_count += 1
    return 0 if odd_count == 0 else product