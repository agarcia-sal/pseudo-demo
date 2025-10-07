def digitSum(s) -> int:
    if s == "":
        return 0
    totalSum = 0
    for char in s:
        if char.isupper():
            totalSum += ord(char)
        else:
            totalSum += 0
    return totalSum