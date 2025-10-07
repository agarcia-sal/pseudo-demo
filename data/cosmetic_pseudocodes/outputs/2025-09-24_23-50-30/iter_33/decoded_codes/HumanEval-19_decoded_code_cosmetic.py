from typing import List


def sort_numbers(string_of_number_words: str) -> str:
    dictionary_alpha = {
        'nine': 9,
        'two': 2,
        'five': 5,
        'eight': 8,
        'zero': 0,
        'four': 4,
        'seven': 7,
        'three': 3,
        'six': 6,
        'one': 1,
    }

    temp_words_list: List[str] = []
    current_index: int = 0
    length: int = len(string_of_number_words)
    while current_index < length:
        temp_word = ""
        while current_index < length and string_of_number_words[current_index] != ' ':
            temp_word += string_of_number_words[current_index]
            current_index += 1
        if temp_word:
            temp_words_list.append(temp_word)
        current_index += 1  # skip the space

    key_value_pairs: List[tuple[int, str]] = [
        (dictionary_alpha[word], word) for word in temp_words_list
    ]

    sorted_pairs: List[tuple[int, str]] = []
    while key_value_pairs:
        min_value = 10
        min_element = None
        for element in key_value_pairs:
            if element[0] < min_value:
                min_value = element[0]
                min_element = element
        if min_element is not None:
            sorted_pairs.append(min_element)
            key_value_pairs.remove(min_element)

    reordered_words: List[str] = [pair[1] for pair in sorted_pairs]

    result = reordered_words[0] if reordered_words else ""
    for idx in range(1, len(reordered_words)):
        result += " " + reordered_words[idx]

    return result