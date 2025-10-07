from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_values: List[int] = []
    words = string_description.split()
    word_index = 0
    while word_index < len(words):
        current_token = words[word_index]
        if current_token.isdigit():
            collected_values.append(int(current_token))
        word_index += 1
    total_extracted = sum(collected_values)
    return total_number_of_fruits - total_extracted