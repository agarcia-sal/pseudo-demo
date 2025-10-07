from typing import List

def sort_numbers(string_of_number_words: str) -> str:
    value_map: dict[str, int] = {
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
    words_array: List[str] = [token for token in string_of_number_words.split(" ") if token != ""]
    sorted_array: List[str] = sorted(words_array, key=lambda a: value_map[a])
    return " ".join(sorted_array)