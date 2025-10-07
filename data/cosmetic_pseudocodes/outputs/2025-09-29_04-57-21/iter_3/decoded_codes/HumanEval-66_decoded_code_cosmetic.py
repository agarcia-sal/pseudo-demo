def digitSum(string_input: str) -> int:
    if not string_input:
        return 0
    totalSum: int = 0
    for singleChar in string_input:
        if 'A' <= singleChar <= 'Z':
            totalSum += ord(singleChar)
    return totalSum