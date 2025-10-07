from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    numbers_storage: List[int] = []
    words_sequence: List[str] = string_description.split(" ")
    current_word_index: int = 0
    while current_word_index < len(words_sequence):
        single_word: str = words_sequence[current_word_index]
        if single_word.isdigit():
            numeric_transform: int = int(single_word)
            numbers_storage.append(numeric_transform)
        current_word_index += 1
    accumulated_sum: int = 0
    for number_element in numbers_storage:
        accumulated_sum += number_element
    return total_number_of_fruits - accumulated_sum