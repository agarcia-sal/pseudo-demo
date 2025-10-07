def digitSum(input_string: str) -> int:
    if input_string == "":
        return 0
    total_sum = 0
    for character in input_string:
        if character.isupper():
            total_sum += ord(character)
    return total_sum