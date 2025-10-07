from typing import List, Dict

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    counts: Dict[int, int] = {}
    for num in list_of_numbers:
        counts[num] = counts.get(num, 0) + 1

    def recurse_filter(
        list_of_numbers: List[int],
        counts: Dict[int, int],
        index: int,
        result: List[int],
    ) -> List[int]:
        if index == len(list_of_numbers):
            return result
        current = list_of_numbers[index]
        if counts[current] <= 1:
            result_prime = result + [current]
        else:
            result_prime = result
        return recurse_filter(list_of_numbers, counts, index + 1, result_prime)

    return recurse_filter(list_of_numbers, counts, 0, [])