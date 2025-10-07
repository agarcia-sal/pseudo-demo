def digitSum(string_input: str) -> int:
    if not string_input:
        return 0
    total_sum = 0
    for character in string_input:
        if 'A' <= character <= 'Z':
            total_sum += ord(character)
    return total_sum