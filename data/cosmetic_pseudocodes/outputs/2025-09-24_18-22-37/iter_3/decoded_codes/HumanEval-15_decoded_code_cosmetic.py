from typing import List

def string_sequence(integer_n: int) -> str:
    accumulator: List[str] = []
    index: int = 0
    while index <= integer_n:
        accumulator.append(str(index))
        index += 1
    result: str = ''
    for i in range(len(accumulator)):
        result += accumulator[i]
        if i < len(accumulator) - 1:
            result += ' '
    return result