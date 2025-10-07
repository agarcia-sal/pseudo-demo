def digitSum(s) -> int:
    if s == "":
        return 0
    total = 0
    for character in s:
        if character.isupper():
            total += ord(character)
        else:
            total += 0
    return total