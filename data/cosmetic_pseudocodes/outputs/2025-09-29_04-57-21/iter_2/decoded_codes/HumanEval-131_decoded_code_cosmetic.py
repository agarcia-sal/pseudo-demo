def digits(input_number: int) -> int:
    accumulator: int = 1
    tally: int = 0
    s: str = str(input_number)
    for index in range(len(s)):
        character: str = s[index]
        numeric_value: int = int(character)
        if numeric_value % 2 != 0:
            accumulator *= numeric_value
            tally += 1
    return accumulator if tally != 0 else 0