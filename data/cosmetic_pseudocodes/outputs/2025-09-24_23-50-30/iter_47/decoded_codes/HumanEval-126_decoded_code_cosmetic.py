from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    alpha = {key: 0 for key in list_of_numbers}  # count occurrences
    idx = 0
    while idx < len(list_of_numbers):
        omega = list_of_numbers[idx]
        alpha[omega] += 1
        idx += 1

    checker = True
    beta = 0
    while beta < len(list_of_numbers) and checker:
        gamma = list_of_numbers[beta]
        if alpha[gamma] > 2:
            checker = False
        beta += 1

    if not checker:
        return False

    if len(list_of_numbers) <= 1:
        return True

    mu = 1
    while mu < len(list_of_numbers):
        if not (list_of_numbers[mu - 1] <= list_of_numbers[mu]):
            return False
        mu += 1

    return True