from typing import List

def by_length(input_list: List[int]) -> List[str]:
    dictionary_of_numbers: dict[int, str] = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One",
    }

    def process_next(index: int, acc: List[str]) -> List[str]:
        if index >= len(input_list):
            return acc
        current_num = input_list[index]
        if current_num in dictionary_of_numbers:
            acc = acc + [dictionary_of_numbers[current_num]]
        return process_next(index + 1, acc)

    input_list.sort(key=lambda item: -item)
    return process_next(0, [])