def digitSum(s: str) -> int:
    if s == "":
        return 0
    totalSum = 0
    lengthOfS = len(s)
    for i in range(lengthOfS):
        char = s[i]
        if char.isupper():
            totalSum += ord(char)
        else:
            totalSum += 0
    return totalSum