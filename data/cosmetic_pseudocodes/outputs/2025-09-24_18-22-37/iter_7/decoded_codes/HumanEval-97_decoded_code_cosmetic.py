def multiply(value_one: int, value_two: int) -> int:
    remainder_one = value_one % 10
    remainder_two = value_two % 10

    abs_remainder_one = abs(remainder_one)
    abs_remainder_two = abs(remainder_two)

    product_result = abs_remainder_one * abs_remainder_two

    return product_result