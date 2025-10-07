def special_factorial(num_input: int) -> int:
    product_current: int = 1
    accumulated_factorial: int = 1
    counter: int = 1
    while counter <= num_input:
        product_current *= counter
        accumulated_factorial *= product_current
        counter += 1
    return accumulated_factorial