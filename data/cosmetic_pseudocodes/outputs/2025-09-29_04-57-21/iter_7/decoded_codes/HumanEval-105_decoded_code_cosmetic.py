from typing import List

def by_length(numbers_list: List[int]) -> List[str]:
    num_word_map: dict[int, str] = {
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

    descending_sorted: List[int] = sorted(numbers_list, reverse=True)

    collected_words: List[str] = []
    idx: int = 0
    while idx < len(descending_sorted):
        current_num: int = descending_sorted[idx]
        if current_num in num_word_map:
            collected_words.append(num_word_map[current_num])
        idx += 1

    return collected_words