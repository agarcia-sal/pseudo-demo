from typing import List, Dict

def by_length(array_of_integers: List[int]) -> List[str]:
    digit_words: Dict[int, str] = {
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
    descending_sorted: List[int] = sorted(array_of_integers, reverse=True)
    result_list: List[str] = []
    for index in range(len(descending_sorted)):
        current_num = descending_sorted[index]
        if current_num not in digit_words:
            continue
        word = digit_words[current_num]
        result_list.append(word)
    return result_list