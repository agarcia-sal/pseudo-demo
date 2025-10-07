from typing import List, Dict

def by_length(numbers_list: List[int]) -> List[str]:
    num_to_word_map: Dict[int, str] = {
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
    result_list: List[str] = [
        num_to_word_map[num] for num in descending_sorted if num in num_to_word_map
    ]
    return result_list