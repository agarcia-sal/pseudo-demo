def is_prime(number: int) -> bool:
    if number < 2:
        return False

    divisor_counter = 2
    while divisor_counter <= number - 2:
        if number % divisor_counter == 0:
            return False
        divisor_counter += 1

    return True