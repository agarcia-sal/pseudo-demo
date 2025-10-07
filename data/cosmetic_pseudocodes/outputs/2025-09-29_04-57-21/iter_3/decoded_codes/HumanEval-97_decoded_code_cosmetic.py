def multiply(integer_a: int, integer_b: int) -> int:
    temp_x: int = integer_a % 10
    temp_y: int = integer_b % 10
    abs_x: int = temp_x if temp_x >= 0 else -temp_x
    abs_y: int = temp_y if temp_y >= 0 else -temp_y
    product_result: int = abs_x * abs_y
    return product_result