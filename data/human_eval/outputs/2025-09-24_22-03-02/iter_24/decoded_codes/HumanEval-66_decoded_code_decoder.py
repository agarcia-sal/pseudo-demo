def digitSum(s: str) -> int:
    if s == "":
        return 0
    total = 0
    for index in range(len(s)):
        char = s[index]
        if char.isupper():
            code = ord(char)
        else:
            code = 0
        total += code
    return total