def digitSum(string_input: str) -> int:
    if string_input == "":
        return 0

    totalValue = 0
    currentIndex = 0
    while currentIndex < len(string_input):
        charItem = string_input[currentIndex]
        if 'A' <= charItem <= 'Z':
            totalValue += ord(charItem)
        currentIndex += 1
    return totalValue