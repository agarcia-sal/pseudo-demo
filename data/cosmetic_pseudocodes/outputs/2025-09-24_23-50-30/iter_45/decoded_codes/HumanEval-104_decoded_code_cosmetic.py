from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def only_odd_digits(num: int) -> bool:
        s = str(num)
        for ch in s:
            if ch in {'0', '2', '4', '6', '8'}:
                return False
        return True

    temp_container: List[int] = []
    for candidate in list_of_positive_integers:
        if only_odd_digits(candidate):
            temp_container.append(candidate)

    sorted_results = sorted(temp_container)
    return sorted_results