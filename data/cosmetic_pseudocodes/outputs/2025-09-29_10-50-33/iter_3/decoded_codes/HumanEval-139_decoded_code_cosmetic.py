def special_factorial(num: int) -> int:
    product_accumulator: int = 1
    nested_factorial: int = 1
    counter: int = 1
    while counter <= num:
        product_accumulator *= counter
        nested_factorial *= product_accumulator
        counter += 1
    return nested_factorial