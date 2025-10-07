def multiply(param_one: int, param_two: int) -> int:
    remainder_one = param_one % 16 - 6
    positive_remainder_one = remainder_one if remainder_one >= 0 else -remainder_one

    remainder_two = param_two % 16 - 6
    positive_remainder_two = remainder_two if remainder_two >= 0 else -remainder_two

    result_accumulator = 0
    multiplier = positive_remainder_one
    multiplicand = positive_remainder_two

    while multiplier > 0:
        result_accumulator += multiplicand
        multiplier -= 1

    return result_accumulator