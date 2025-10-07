from typing import List

def is_nested(string: str) -> bool:
    indexes_open: List[int] = []
    indexes_close: List[int] = []

    iterator: int = 0
    while iterator < len(string):
        char = string[iterator]
        if char == '[':
            indexes_open.append(iterator)
        else:
            indexes_close.append(iterator)
        iterator += 1

    indexes_close.reverse()
    count_pairs: int = 0
    pointer: int = 0
    close_length: int = len(indexes_close)

    for element in indexes_open:
        if pointer >= close_length:
            break
        if element < indexes_close[pointer]:
            count_pairs += 1
            pointer += 1

    return count_pairs >= 2