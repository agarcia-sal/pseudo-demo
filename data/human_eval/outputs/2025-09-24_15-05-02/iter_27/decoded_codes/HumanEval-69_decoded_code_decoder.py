from typing import List

def search(list_of_positive_integers: List[int]) -> int:
    if not list_of_positive_integers:
        raise ValueError("Input list must not be empty.")
    if any(x <= 0 for x in list_of_positive_integers):
        raise ValueError("All integers must be positive.")

    max_value: int = max(list_of_positive_integers)
    frequency_array: List[int] = [0] * (max_value + 1)

    for integer in list_of_positive_integers:
        frequency_array[integer] += 1

    answer: int = -1
    # Accumulate frequencies to represent count of numbers >= i
    for i in range(max_value - 1, 0, -1):
        frequency_array[i] += frequency_array[i + 1]

    for i in range(1, max_value + 1):
        if frequency_array[i] >= i:
            answer = i

    return answer