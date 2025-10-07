from typing import List

def sort_numbers(string_of_number_words: str) -> str:
    digits_dictionary: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    words_array: List[str] = [token for token in string_of_number_words.split(" ") if token]

    # Sort words_array in-place using the digit values for comparison
    words_array.sort(key=lambda word: digits_dictionary[word])

    return " ".join(words_array)