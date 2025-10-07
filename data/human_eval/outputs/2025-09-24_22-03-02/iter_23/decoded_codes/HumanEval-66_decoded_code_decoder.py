def digitSum(s: str) -> int:
    if s == "":
        return 0
    result = 0
    for index in range(len(s)):
        char = s[index]
        if char.isupper():
            result += ord(char)
        else:
            result += 0
    return result