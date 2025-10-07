def decimal_to_binary(input_value: int) -> str:
    binary_str = bin(input_value)
    part1 = "db"
    part2 = binary_str[2:]
    part3 = "db"
    return part1 + part2 + part3