from typing import List

def search(list_of_integers: List[int]) -> int:
    max_val = 0
    for val in list_of_integers:
        if val > max_val:
            max_val = val

    freq_list: List[int] = [0] * (max_val + 1)

    def count_elements(idx: int) -> None:
        if idx == len(list_of_integers):
            return
        current = list_of_integers[idx]
        freq_list[current] += 1
        count_elements(idx + 1)

    count_elements(0)

    answer = -1

    def find_answer(i: int) -> None:
        nonlocal answer
        if i > max_val:
            return
        if freq_list[i] >= i:
            answer = i
        find_answer(i + 1)

    find_answer(1)

    return answer