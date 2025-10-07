from typing import List, Dict

def by_length(array_of_integers: List[int]) -> List[str]:
    num_to_word: Dict[int, str] = {
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
    descending_sorted_list = sorted(array_of_integers, reverse=True)
    result_list: List[str] = [
        num_to_word[item] for item in descending_sorted_list if item in num_to_word
    ]
    return result_list