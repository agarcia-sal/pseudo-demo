def digits(number: int) -> int:
    accumulator: int = 1
    tally: int = 0
    stringified: str = str(number)
    index: int = 0
    while index < len(stringified):
        char_element: str = stringified[index]
        converted_digit: int = int(char_element)
        if converted_digit % 2 != 0:
            accumulator *= converted_digit
            tally += 1
        index += 1
    return 0 if tally == 0 else accumulator