from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    alpha_collection: List[str] = string_s.split(" ")
    accumulation: List[str] = []
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for current_item in alpha_collection:
        count_c = sum(
            1 for letter in current_item
            if letter.lower() not in vowels
        )
        if count_c == natural_number_n:
            accumulation.append(current_item)

    return accumulation