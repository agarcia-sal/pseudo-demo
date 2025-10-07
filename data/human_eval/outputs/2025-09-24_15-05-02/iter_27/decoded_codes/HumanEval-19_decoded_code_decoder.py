from typing import Dict

def sort_numbers(numbers_string: str) -> str:
    value_map: Dict[str, int] = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    list_of_number_words = [word for word in numbers_string.split(" ") if word]

    # Validate that all words are valid keys in value_map
    if any(word not in value_map for word in list_of_number_words):
        raise ValueError("Input contains invalid number words.")

    sorted_number_words = sorted(list_of_number_words, key=lambda word: value_map[word])

    return " ".join(sorted_number_words)