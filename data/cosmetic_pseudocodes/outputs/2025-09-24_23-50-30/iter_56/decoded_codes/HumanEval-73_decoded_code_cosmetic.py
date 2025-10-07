from typing import List


def smallest_change(list_of_numbers: List[int]) -> int:
    answer_counter: int = 0
    length: int = len(list_of_numbers)
    limit: int = (length - (length % 2)) // 2  # number of pairs to check

    iterator_index: int = 0
    while iterator_index < limit:
        if list_of_numbers[iterator_index] != list_of_numbers[length - 1 - iterator_index]:
            answer_counter += 1
            break
        iterator_index += 1

    return answer_counter