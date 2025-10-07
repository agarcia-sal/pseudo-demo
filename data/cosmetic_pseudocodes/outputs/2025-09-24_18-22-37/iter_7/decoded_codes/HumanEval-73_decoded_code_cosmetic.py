from typing import List

def smallest_change(list_of_numbers: List[int]) -> int:
    result: int = 0
    counter: int = 0
    limit: int = (len(list_of_numbers) // 2) - 1  # middle index to compare pairs

    while counter <= limit:
        left_element: int = list_of_numbers[counter]
        right_element_index: int = len(list_of_numbers) - counter - 1
        right_element: int = list_of_numbers[right_element_index]

        if left_element != right_element:
            result += 1
        counter += 1

    return result