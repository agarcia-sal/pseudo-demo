from typing import List

def by_length(numbers_list: List[int]) -> List[str]:
    number_names = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One"
    }
    descending_sorted = sorted(numbers_list, reverse=True)
    translated: List[str] = []
    index = 0
    while index < len(descending_sorted):
        current_number = descending_sorted[index]
        if current_number in number_names:
            translated.append(number_names[current_number])
        index += 1
    return translated