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

    word_collection: List[str] = [segment for segment in string_of_number_words.split(' ') if segment]

    def compare_words(a: str, b: str) -> int:
        return value_map[a] - value_map[b]

    ordered_words: List[str] = sorted(word_collection, key=lambda w: value_map[w])

    result_string: str = ' '.join(ordered_words)

    return result_string