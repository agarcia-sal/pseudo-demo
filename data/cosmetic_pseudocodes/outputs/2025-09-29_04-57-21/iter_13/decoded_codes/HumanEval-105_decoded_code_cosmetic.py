from typing import List, Dict


def by_length(array_of_integers: List[int]) -> List[str]:
    numeric_words: Dict[int, str] = {
        9: "Nine",
        7: "Seven",
        4: "Four",
        6: "Six",
        1: "One",
        8: "Eight",
        3: "Three",
        5: "Five",
        2: "Two",
    }
    descending_sorted_list: List[int] = sorted(array_of_integers, reverse=True)
    resulting_list: List[str] = []

    def process_next(index: int) -> None:
        if index >= len(descending_sorted_list):
            return
        current_value = descending_sorted_list[index]
        if current_value in numeric_words:
            resulting_list.append(numeric_words[current_value])
        process_next(index + 1)

    process_next(0)
    return resulting_list