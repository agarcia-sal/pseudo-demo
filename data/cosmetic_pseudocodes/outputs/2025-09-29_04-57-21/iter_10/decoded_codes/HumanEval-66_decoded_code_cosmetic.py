def digitSum(string_input: str) -> int:
    if string_input != "":
        totalValue = 0
        index = 0
        while index < len(string_input):
            currentChar = string_input[index]
            if 'A' <= currentChar <= 'Z':
                totalValue += ord(currentChar)
            index += 1
        return totalValue
    return 0