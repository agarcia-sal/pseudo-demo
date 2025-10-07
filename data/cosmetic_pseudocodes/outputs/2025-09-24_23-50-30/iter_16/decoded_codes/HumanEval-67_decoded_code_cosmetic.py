from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def parse_digits(words: List[str], index: int, collected: List[int]) -> List[int]:
        if index >= len(words):
            return collected
        current_element = words[index]
        if current_element.isdigit():
            collected.append(int(current_element))
        return parse_digits(words, index + 1, collected)

    words_list = string_description.split(" ")
    gathered_numbers = parse_digits(words_list, 0, [])
    sum_accumulated = sum(gathered_numbers)
    return total_number_of_fruits - sum_accumulated