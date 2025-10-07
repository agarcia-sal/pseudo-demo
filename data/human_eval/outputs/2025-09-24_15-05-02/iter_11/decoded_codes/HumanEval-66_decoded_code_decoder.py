def digitSum(string_s):
    if not string_s:
        return 0
    total_sum = 0
    for character in string_s:
        if character.isupper():
            total_sum += ord(character)
    return total_sum