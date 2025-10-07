from typing import List


def fizz_buzz(digit_p: int) -> int:
    collection_x: List[int] = []
    index_y: int = 0
    while index_y < digit_p:
        if (index_y % 11 == 0) or (index_y % 13 == 0):
            collection_x.append(index_y)
        index_y += 1

    string_accumulator: str = ""
    iterator_z: int = 0
    while iterator_z < len(collection_x):
        string_accumulator += str(collection_x[iterator_z])
        iterator_z += 1

    counter_m: int = 0
    pointer_n: int = 0
    while pointer_n < len(string_accumulator):
        if not (string_accumulator[pointer_n] != '7'):
            counter_m += 1
        pointer_n += 1

    return counter_m