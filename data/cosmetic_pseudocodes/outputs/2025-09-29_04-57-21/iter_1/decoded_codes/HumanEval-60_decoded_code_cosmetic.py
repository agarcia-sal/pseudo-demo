def sum_to_n(integer_n: int) -> int:
    total = 0
    counter = 0
    while counter <= integer_n:
        total += counter
        counter += 1
    return total