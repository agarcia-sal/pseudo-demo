def digitSum(s: str) -> int:
    if not s:
        return 0

    total_sum: int = 0
    for character in s:
        if character.isupper():
            total_sum += ord(character)

    return total_sum