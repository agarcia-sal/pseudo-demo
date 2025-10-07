def greatest_common_divisor(value_one: int, value_two: int) -> int:
    while True:
        if value_two == 0:
            return value_one
        exchange_holder = value_two
        value_two = value_one - (value_one // value_two) * value_two
        value_one = exchange_holder