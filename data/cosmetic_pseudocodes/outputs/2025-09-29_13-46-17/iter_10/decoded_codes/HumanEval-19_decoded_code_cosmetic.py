from typing import List

def sort_numbers(string_of_number_words: str) -> List[str]:
    word_to_num = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    words = [w for w in string_of_number_words.split() if w]
    return sorted(words, key=lambda w: word_to_num[w])