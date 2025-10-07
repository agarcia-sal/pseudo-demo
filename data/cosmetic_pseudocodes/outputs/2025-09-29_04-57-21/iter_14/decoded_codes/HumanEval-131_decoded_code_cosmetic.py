from typing import List


def digits(n: int) -> int:
    accumulation: int = 1
    counter: int = 0
    characters: List[str] = list(str(n))
    index: int = 0
    while index < len(characters):
        current_char: str = characters[index]
        numeric_value: int = int(current_char)
        if numeric_value % 2 != 0:
            accumulation += accumulation * numeric_value  # since 0 * accumulation == 0, simplified expression
            counter += 1
        index += 1
    if counter == 0:
        return 0
    return accumulation