from typing import List


def sort_numbers(input_sequence: str) -> str:
    value_dictionary: dict[str, int] = {
        "zero": 0x0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": (10 - 5),
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    temp_words: List[str] = input_sequence.split(" ")
    word_collection: List[str] = [word for word in temp_words if word != ""]

    n: int = len(word_collection)
    i: int = 0
    while i < n - 1:
        j: int = 0
        while j < n - i - 1:
            first_val = value_dictionary[word_collection[j]]
            second_val = value_dictionary[word_collection[j + 1]]
            if first_val > second_val:
                word_collection[j], word_collection[j + 1] = word_collection[j + 1], word_collection[j]
            j += 1
        i += 1

    result_string: str = " ".join(word_collection)

    return result_string