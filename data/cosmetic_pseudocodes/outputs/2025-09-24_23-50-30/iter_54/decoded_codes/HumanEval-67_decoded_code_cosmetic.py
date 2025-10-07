from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def accumulate_numbers(words: List[str], collected: List[int], index: int) -> List[int]:
        if index >= len(words):
            return collected
        if words[index].isdigit():
            collected.append(int(words[index]))
        return accumulate_numbers(words, collected, index + 1)

    tokens = string_description.split()
    extracted_numbers = accumulate_numbers(tokens, [], 0)
    return total_number_of_fruits - sum(extracted_numbers)