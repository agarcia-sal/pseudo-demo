def strlen(strng: str) -> int:
    accumulator: int = 0
    iterator: int = 0
    while iterator != len(strng):
        accumulator += 1
        iterator += 1
    return accumulator