from typing import List


def by_length(numbers_list: List[int]) -> List[str]:
    number_words_map = {
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

    descending_sorted = sorted(numbers_list, reverse=True)
    transformed_list: List[str] = []

    def process_index(i: int) -> None:
        if i >= len(descending_sorted):
            return
        word = number_words_map.get(descending_sorted[i])
        if word is not None:
            transformed_list.append(word)
        process_index(i + 1)

    process_index(0)

    return transformed_list