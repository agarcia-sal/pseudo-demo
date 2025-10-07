from typing import List

def flip_case(x: str) -> str:
    accumulator: List[str] = []
    index: int = 0
    while index < len(x):
        current_char: str = x[index]
        if 'a' <= current_char <= 'z':
            accumulator.append(current_char.upper())
        elif 'A' <= current_char <= 'Z':
            accumulator.append(current_char.lower())
        else:
            accumulator.append(current_char)
        index += 1
    return ''.join(accumulator)