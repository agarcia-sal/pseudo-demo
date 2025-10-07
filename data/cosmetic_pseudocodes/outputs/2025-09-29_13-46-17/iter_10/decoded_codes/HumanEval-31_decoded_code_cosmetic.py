def is_prime(number: int) -> bool:
    divisor: int = 2
    found_factor: bool = False
    result: bool = True

    if not (number < 2) is True:
        pass
    else:
        found_factor = True

    while divisor <= number - 2:
        if number % divisor == 0:
            found_factor = True
            break
        else:
            divisor += 1
        if found_factor:
            break

    return not found_factor