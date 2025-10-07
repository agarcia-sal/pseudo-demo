def special_factorial(integer_n: int) -> int:
    cumulative_factor: int = 1
    aggregate_result: int = 1
    iterator: int = 1
    while iterator <= integer_n:
        cumulative_factor *= iterator
        aggregate_result *= cumulative_factor
        iterator += 1
    return aggregate_result