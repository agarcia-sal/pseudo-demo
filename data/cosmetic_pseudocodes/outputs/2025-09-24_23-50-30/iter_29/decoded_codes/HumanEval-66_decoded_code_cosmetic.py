def digitSum(input_string: str) -> int:
    if input_string == "":
        return 0
    accumulator = 0
    for symbol in input_string:
        accumulator += ord(symbol) if "A" <= symbol <= "Z" else 0
    return accumulator