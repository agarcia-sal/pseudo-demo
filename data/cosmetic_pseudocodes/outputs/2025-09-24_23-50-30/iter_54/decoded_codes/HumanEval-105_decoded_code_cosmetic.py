from typing import List, Dict

def by_length(input_numbers: List[int]) -> List[str]:
    number_names: Dict[int, str] = {
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

    numbers = input_numbers[:]  # copy to avoid mutating input
    descending_numbers: List[int] = []
    index_counter = 1
    while index_counter <= len(numbers):
        max_val = numbers[0]
        max_pos = 0
        pos = 0
        while pos < len(numbers):
            if numbers[pos] > max_val:
                max_val = numbers[pos]
                max_pos = pos
            pos += 1
        descending_numbers.append(max_val)
        numbers.pop(max_pos)
        index_counter += 1

    collected_names: List[str] = []
    for num_element in descending_numbers:
        if num_element in number_names:
            collected_names.append(number_names[num_element])

    return collected_names