def multiply(p_num1: int, p_num2: int) -> int:
    remainder1: int = p_num1 % 0xA
    remainder2: int = p_num2 % 0xA
    abs_part1: int = remainder1 if remainder1 >= 0 else -remainder1
    abs_part2: int = remainder2 if remainder2 >= 0 else -remainder2
    product_result: int = abs_part1 * abs_part2
    return product_result