def digitSum(s: str) -> int:
    if s == '':
        return 0

    totalSum = 0
    for character in s:
        if character.isupper():
            totalSum += ord(character)

    return totalSum