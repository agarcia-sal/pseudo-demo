from typing import Dict

def sort_numbers(string_of_number_words: str) -> str:
    map_values: Dict[str, int] = {
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
    array_words = [token for token in string_of_number_words.split(' ') if token != '']

    index = 1
    while index < len(array_words):
        key_word = array_words[index]
        position = index - 1
        while position >= 0 and map_values[array_words[position]] > map_values[key_word]:
            array_words[position + 1] = array_words[position]
            position -= 1
        array_words[position + 1] = key_word
        index += 1
    return ' '.join(array_words)