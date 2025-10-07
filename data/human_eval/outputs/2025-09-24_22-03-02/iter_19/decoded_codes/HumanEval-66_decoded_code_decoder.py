def digitSum(s: str) -> int:
    if s == "":
        return 0
    total = 0
    for index in range(len(s)):
        char = s[index]
        if char.isupper():
            total += ord(char)
        else:
            total += 0
    return total