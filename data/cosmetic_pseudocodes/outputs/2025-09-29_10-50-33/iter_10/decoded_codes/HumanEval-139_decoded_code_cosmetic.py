def special_factorial(integer_n: int) -> int:
    product_accumulator: int = 1
    cumulative_result: int = 1
    index_counter: int = 1

    while index_counter <= integer_n:
        product_accumulator *= index_counter
        cumulative_result *= product_accumulator
        index_counter += 1

    return cumulative_result