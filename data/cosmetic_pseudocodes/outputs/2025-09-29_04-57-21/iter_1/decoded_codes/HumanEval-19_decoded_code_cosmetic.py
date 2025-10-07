from typing import List

def sort_numbers(string_of_number_words: str) -> str:
    value_map: dict[str, int] = {
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

    words_array: List[str] = [token for token in string_of_number_words.split(" ") if token != ""]

    def compare_words(a: str, b: str) -> int:
        return value_map[a] - value_map[b]

    n: int = len(words_array)
    for i in range(n):
        for j in range(n - i - 1):
            if compare_words(words_array[j], words_array[j + 1]) > 0:
                words_array[j], words_array[j + 1] = words_array[j + 1], words_array[j]

    result_string: str = " ".join(words_array)
    return result_string