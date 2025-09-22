def convert_string_to_numeric_string():
    inputString = input().strip()
    currentIndex = 0
    result = ""

    while currentIndex < len(inputString):
        if inputString[currentIndex] == '.':
            result += '0'
            currentIndex += 1
        elif currentIndex + 1 < len(inputString) and inputString[currentIndex + 1] == '.':
            result += '1'
            currentIndex += 2
        else:
            result += '2'
            currentIndex += 2

    print(result)

convert_string_to_numeric_string()


def convert_string_to_numeric_string():
    inputString = input().strip()
    idx = 0
    result = []

    while idx < len(inputString):
        if inputString[idx] == '.':
            result.append('0')
            idx += 1
        elif idx + 1 < len(inputString) and inputString[idx + 1] == '.':
            result.append('1')
            idx += 2
        else:
            result.append('2')
            idx += 2

    print(''.join(result))

convert_string_to_numeric_string()
