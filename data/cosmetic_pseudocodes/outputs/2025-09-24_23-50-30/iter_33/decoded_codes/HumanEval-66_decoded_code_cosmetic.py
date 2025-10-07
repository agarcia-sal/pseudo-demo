def digitSum(alpha_input: str) -> int:
    total_accumulator: int = 0
    for each_element in alpha_input:
        if 'A' <= each_element <= 'Z':
            total_accumulator += ord(each_element)
    return total_accumulator