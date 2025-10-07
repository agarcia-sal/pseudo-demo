def largest_divisor(number: int) -> int:
    found_divisor = False
    candidate = 0
    counter = number - 1
    while counter > 0 and not found_divisor:
        remainder = number - ((number // counter) * counter)
        if remainder == 0:
            candidate = counter
            found_divisor = True
        else:
            counter -= 1
    return candidate