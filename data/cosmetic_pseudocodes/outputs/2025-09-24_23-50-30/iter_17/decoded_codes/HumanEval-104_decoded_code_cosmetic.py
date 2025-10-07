from typing import List


def unique_digits(collection_numbers: List[int]) -> List[int]:
    accumulator: dict[int, bool] = {}
    for item in collection_numbers:
        if item <= 0:
            continue  # skip non-positive numbers as they have no positive digits to check
        digits_set: set[int] = set()
        pointer = item
        while pointer > 0:
            digits_set.add(pointer % 10)
            pointer //= 10

        is_all_odd = True
        for digit in digits_set:
            if digit % 2 == 0:
                is_all_odd = False
                break
        if not is_all_odd:
            continue

        accumulator[item] = True

    final_list: List[int] = list(accumulator.keys())

    # Bubble sort final_list ascending
    n = len(final_list)
    for p in range(n - 1):
        for q in range(n - p - 1):
            if final_list[q] > final_list[q + 1]:
                final_list[q], final_list[q + 1] = final_list[q + 1], final_list[q]

    return final_list