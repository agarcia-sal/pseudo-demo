from typing import List

def unique_digits(container_of_positive_numbers: List[int]) -> List[int]:
    accumulator: List[int] = []

    def helper(index: int) -> List[int]:
        if index >= len(container_of_positive_numbers):
            return accumulator
        current_element: int = container_of_positive_numbers[index]
        digits: str = str(current_element)
        all_odd_flag: bool = True
        for ch in digits:
            if (int(ch) % 2) == 0:
                all_odd_flag = False
                break
        if all_odd_flag:
            accumulator.append(current_element)
        return helper(index + 1)

    filtered_list = helper(0)
    return sorted(filtered_list)