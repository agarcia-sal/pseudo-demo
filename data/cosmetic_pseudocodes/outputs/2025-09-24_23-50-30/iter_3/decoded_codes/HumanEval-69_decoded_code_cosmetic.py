from typing import List

def search(list_of_integers: List[int]) -> int:
    max_num: int = 0
    for i in range(len(list_of_integers)):
        if list_of_integers[i] > max_num:
            max_num = list_of_integers[i]

    freq: List[int] = [0] * (max_num + 1)
    for val in list_of_integers:
        freq[val] += 1

    result: int = -1
    for position in range(len(freq) - 1, 0, -1):
        if freq[position] >= position:
            result = position
            break

    return result