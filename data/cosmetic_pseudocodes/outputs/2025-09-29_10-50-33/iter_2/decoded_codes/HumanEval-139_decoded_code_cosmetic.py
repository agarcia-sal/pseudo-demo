def special_factorial(number_m: int) -> int:
    product_current: int = 1
    aggregate_product: int = 1
    for counter in range(1, number_m + 1):
        product_current *= counter
        aggregate_product *= product_current
    return aggregate_product