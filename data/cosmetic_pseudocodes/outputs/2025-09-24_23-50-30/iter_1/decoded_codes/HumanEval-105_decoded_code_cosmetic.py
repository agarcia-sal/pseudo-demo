from typing import List

def by_length(array_of_integers: List[int]) -> List[str]:
    number_words: dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    temp_array: List[int] = sorted(array_of_integers, reverse=True)
    result_list: List[str] = []
    index: int = 0
    while index < len(temp_array):
        current_value: int = temp_array[index]
        if current_value in number_words:
            result_list.append(number_words[current_value])
        index += 1
    return result_list