from typing import Dict

def sort_numbers(string_of_number_words: str) -> str:
    value_dictionary: Dict[str, int] = {
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

    word_array = [token for token in string_of_number_words.split(' ') if token != '']

    index = 0
    while index < len(word_array) - 1:
        position = index + 1
        while position < len(word_array):
            if value_dictionary[word_array[index]] > value_dictionary[word_array[position]]:
                word_array[index], word_array[position] = word_array[position], word_array[index]
            position += 1
        index += 1

    result_string = ''
    item_iterator = 0
    while item_iterator < len(word_array):
        result_string += word_array[item_iterator]
        if item_iterator != len(word_array) - 1:
            result_string += ' '
        item_iterator += 1

    return result_string