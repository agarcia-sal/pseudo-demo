from typing import List


def sort_numbers(input_string: str) -> str:
    value_dictionary: dict[str, int] = {
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

    temp_words: List[str] = input_string.split(' ')
    filtered_words: List[str] = []

    index_var: int = 0
    while index_var < len(temp_words):
        current_word = temp_words[index_var]
        if current_word != '':
            filtered_words.append(current_word)
        index_var += 1

    word_sorted: List[str] = []
    while len(filtered_words) > 0:
        min_word = filtered_words[0]
        min_value = value_dictionary[min_word]
        i: int = 1
        while i < len(filtered_words):
            word = filtered_words[i]
            word_value = value_dictionary[word]
            if word_value < min_value:
                min_word = word
                min_value = word_value
            i += 1
        word_sorted.append(min_word)

        new_filtered: List[str] = []
        j: int = 0
        while j < len(filtered_words):
            if filtered_words[j] != min_word:
                new_filtered.append(filtered_words[j])
            j += 1
        filtered_words = new_filtered

    result_string: str = ''
    k: int = 0
    while k < len(word_sorted):
        if k == 0:
            result_string = word_sorted[k]
        else:
            result_string += ' ' + word_sorted[k]
        k += 1

    return result_string