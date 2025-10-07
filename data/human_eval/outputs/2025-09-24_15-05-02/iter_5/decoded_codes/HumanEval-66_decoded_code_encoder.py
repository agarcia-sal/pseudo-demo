def digitSum(s: str) -> int:
    if s == "":
        return 0
    total_sum = 0
    for char in s:
        if char.isupper():
            total_sum += ord(char)
    return total_sum