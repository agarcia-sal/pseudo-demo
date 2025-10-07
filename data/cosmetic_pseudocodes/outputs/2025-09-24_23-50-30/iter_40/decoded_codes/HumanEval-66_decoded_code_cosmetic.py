def digitSum(parameter_one: str) -> int:
    if parameter_one == "":
        return 0
    total_value: int = 0
    for current_element in parameter_one:
        if 'A' <= current_element <= 'Z':
            total_value += ord(current_element)
    return total_value