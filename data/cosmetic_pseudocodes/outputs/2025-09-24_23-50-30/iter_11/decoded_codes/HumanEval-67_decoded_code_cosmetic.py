import re
from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def accumulate_numbers(words: List[str], index: int, acc: int) -> int:
        if index >= len(words):
            return acc
        token = words[index]
        acc += int(token) if re.fullmatch(r"\d+", token) else 0
        return accumulate_numbers(words, index + 1, acc)

    components = string_description.split(" ")
    collected_sum = accumulate_numbers(components, 0, 0)
    return total_number_of_fruits - collected_sum