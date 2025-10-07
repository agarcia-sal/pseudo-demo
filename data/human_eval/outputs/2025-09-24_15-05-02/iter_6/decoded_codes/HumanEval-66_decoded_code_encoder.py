def digitSum(string_input: str) -> int:
    if not string_input:
        return 0
    total_sum = 0
    for character in string_input:
        if character.isupper():
            total_sum += ord(character)
        else:
            total_sum += 0
    return total_sum