from typing import List

def by_length(array_of_integers: List[int]) -> List[str]:
    number_to_word: dict[int, str] = {
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
    sorted_array: List[int] = sorted(array_of_integers, reverse=True)
    result: List[str] = [number_to_word[num] for num in sorted_array if num in number_to_word]
    return result