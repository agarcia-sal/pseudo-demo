def sum_to_n(integer_n: int) -> int:
    accumulator: int = 0
    count: int = 0
    while count <= integer_n:
        accumulator += count
        count += 1
    return accumulator