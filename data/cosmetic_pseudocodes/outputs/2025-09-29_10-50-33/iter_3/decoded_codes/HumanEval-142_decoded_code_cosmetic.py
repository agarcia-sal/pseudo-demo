from typing import List, Generator


def sum_squares(array_of_numbers: List[int]) -> Generator[int, None, None]:
    temp_collection: List[int] = []

    cursor: int = 0
    while cursor < len(array_of_numbers):
        if cursor % 3 != 0:
            if cursor % 4 == 0:
                temp_collection.append(array_of_numbers[cursor] ** 3)
            else:
                temp_collection.append(array_of_numbers[cursor])
        else:
            temp_collection.append(array_of_numbers[cursor] ** 2)
        cursor += 1

    accumulator: int = 0
    idx: int = 0
    while idx < len(temp_collection):
        accumulator += temp_collection[idx]
        idx += 1

    yield accumulator