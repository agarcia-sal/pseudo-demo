def digitSum(string_input: str) -> int:
    if not string_input:
        return 0
    sum_of_uppercase = 0
    for character in string_input:
        if character.isupper():
            sum_of_uppercase += ord(character)
    return sum_of_uppercase