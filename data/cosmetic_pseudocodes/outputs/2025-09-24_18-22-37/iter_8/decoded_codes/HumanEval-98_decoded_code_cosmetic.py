def count_upper(string_input: str) -> int:
    accumulator: int = 0
    currentPosition: int = 0
    inputLength: int = len(string_input)

    while currentPosition < inputLength:
        currentChar: str = string_input[currentPosition]
        if currentChar in {'A', 'E', 'I', 'O', 'U'}:
            accumulator += 1
        currentPosition += 2

    return accumulator