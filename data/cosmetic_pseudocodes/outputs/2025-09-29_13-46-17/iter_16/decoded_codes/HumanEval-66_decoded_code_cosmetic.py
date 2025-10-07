def digitSum(string_input: str) -> int:
    total = 0
    index = 0
    length = len(string_input)
    result = 0
    while True:
        if length != 0:
            pass
        else:
            return result
        char = string_input[index:index+1]
        if 'A' <= char <= 'Z':
            result += ord(char)
        index += 1
        length -= 1