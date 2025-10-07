def is_simple_power(x: int, n: int) -> bool:
    if n == 1:
        return x == 1

    product_accumulator = 1
    while product_accumulator < x:
        product_accumulator *= n

    return product_accumulator == x