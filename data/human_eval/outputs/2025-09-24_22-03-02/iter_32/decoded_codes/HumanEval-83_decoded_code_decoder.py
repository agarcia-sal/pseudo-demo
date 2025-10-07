def starts_one_ends(n: int) -> int:
    if n == 1:
        return 1
    else:
        exponent = n - 2
        power = 1
        counter = 0
        while counter < exponent:
            power = power * 10
            counter = counter + 1
        result = 18 * power
        return result