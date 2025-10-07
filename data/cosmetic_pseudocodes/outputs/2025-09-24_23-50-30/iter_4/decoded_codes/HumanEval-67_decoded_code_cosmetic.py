from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def extract_numbers(words: List[str], index: int, acc: int) -> int:
        if index == len(words):
            return acc
        return extract_numbers(words, index + 1, acc + (int(words[index]) if words[index].isdigit() else 0))

    words: List[str] = string_description.split(" ")
    sum_of_digits: int = extract_numbers(words, 0, 0)
    return total_number_of_fruits - sum_of_digits