from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def contains_only_odd(num: int) -> bool:
        if num == 0:
            return True
        return (num % 10) % 2 == 1 and contains_only_odd(num // 10)

    filtered_elements: List[int] = []
    index: int = 0
    while index < len(list_of_positive_integers):
        if contains_only_odd(list_of_positive_integers[index]):
            filtered_elements.append(list_of_positive_integers[index])
        index += 1

    return sorted(filtered_elements)