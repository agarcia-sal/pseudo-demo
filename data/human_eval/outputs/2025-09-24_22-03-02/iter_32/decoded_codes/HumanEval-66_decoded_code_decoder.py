def digitSum(s: str) -> int:
    if s == "":
        return 0
    total = 0
    index = 0
    length = len(s)
    while index < length:
        char = s[index]
        if char.isupper():
            ascii_value = ord(char)
            total += ascii_value
        else:
            total += 0
        index += 1
    return total