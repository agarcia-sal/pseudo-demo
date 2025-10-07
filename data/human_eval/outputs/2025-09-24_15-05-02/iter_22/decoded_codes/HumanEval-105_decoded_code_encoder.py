from typing import List

def by_length(array_of_integers: List[int]) -> List[str]:
    digit_to_name_map = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    sorted_descending_array = sorted(array_of_integers, reverse=True)
    result_array: List[str] = []
    for integer_value in sorted_descending_array:
        if integer_value in digit_to_name_map:
            result_array.append(digit_to_name_map[integer_value])
    return result_array