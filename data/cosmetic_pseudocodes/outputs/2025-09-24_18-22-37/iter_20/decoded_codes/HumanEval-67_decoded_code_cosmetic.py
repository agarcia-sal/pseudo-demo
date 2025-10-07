from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    words: List[str] = string_description.split(" ")
    number_collector: List[int] = []

    word_index: int = 0
    count_words: int = len(words)

    while word_index < count_words:
        current_word: str = words[word_index]
        if not current_word.isdigit():
            word_index += 1
            continue
        numeric_value: int = int(current_word)
        number_collector.append(numeric_value)
        word_index += 1

    accumulated_sum: int = 0
    index_counter: int = 0
    length_numbers: int = len(number_collector)

    while index_counter < length_numbers:
        value_to_add: int = number_collector[index_counter]
        accumulated_sum += value_to_add
        index_counter += 1

    difference_result: int = total_number_of_fruits - accumulated_sum
    return difference_result