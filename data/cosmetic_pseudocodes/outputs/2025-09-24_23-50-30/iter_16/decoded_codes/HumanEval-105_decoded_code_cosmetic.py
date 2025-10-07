from typing import List

def by_length(list_of_values: List[int]) -> List[str]:
    map_string_numbers: dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    def helper(index: int, acc: List[str]) -> List[str]:
        if index > len(list_of_values):
            return acc
        current_value = list_of_values[index - 1]  # zero-based indexing in Python
        acc_extended = acc + [map_string_numbers[current_value]] if current_value in map_string_numbers else acc
        return helper(index + 1, acc_extended)

    descending_sorted = sorted(list_of_values, reverse=True)  # a < b means ascending, so reverse=True for descending
    # but descending_sorted is unused per pseudocode logic, so we keep the exact flow

    return helper(1, [])