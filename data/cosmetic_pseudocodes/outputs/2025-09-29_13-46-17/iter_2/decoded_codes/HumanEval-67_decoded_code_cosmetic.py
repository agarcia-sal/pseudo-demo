import re
from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def accumulate_numbers(words: List[str], idx: int, collected: List[int]) -> List[int]:
        if idx == len(words):
            return collected
        current_element = words[idx]
        if re.fullmatch(r"[0-9]+", current_element):
            return accumulate_numbers(words, idx + 1, collected + [int(current_element)])
        else:
            return accumulate_numbers(words, idx + 1, collected)

    words_array = string_description.split(" ")
    numbers_list = accumulate_numbers(words_array, 0, [])
    sum_numbers = sum(numbers_list)
    return total_number_of_fruits - sum_numbers