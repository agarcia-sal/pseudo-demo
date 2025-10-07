from typing import List


def unique_digits(sequence_of_pos_integers: List[int]) -> List[int]:
    def is_odd_digits(number: int, acc: bool) -> bool:
        if number == 0:
            return acc
        last_digit = number % 10
        if last_digit % 2 == 0:
            return False
        else:
            return is_odd_digits(number // 10, acc and True)

    collected_elements: List[int] = []
    idx = 0

    while idx < len(sequence_of_pos_integers):
        candidate = sequence_of_pos_integers[idx]
        if is_odd_digits(candidate, True):
            collected_elements.append(candidate)
        idx += 1

    def bubble_sort(arr: List[int], n: int) -> List[int]:
        if n <= 1:
            return arr
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return bubble_sort(arr, n - 1)

    sorted_result = bubble_sort(collected_elements, len(collected_elements))
    return sorted_result