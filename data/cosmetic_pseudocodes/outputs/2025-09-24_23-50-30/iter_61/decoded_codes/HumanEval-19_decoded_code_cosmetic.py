from typing import List


def sort_numbers(string_of_number_words: str) -> str:
    dict_alpha: dict[str, int] = {
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
    words_list: List[str] = []
    index_cursor: int = 0
    temp_str: str = ''

    while index_cursor < len(string_of_number_words):
        current_char: str = string_of_number_words[index_cursor]

        if current_char != ' ':
            temp_str += current_char
        else:
            if len(temp_str) > 0:
                words_list.append(temp_str)
                temp_str = ''
        index_cursor += 1
    if len(temp_str) > 0:
        words_list.append(temp_str)

    def insertion_sort(arr: List[str], length_n: int) -> None:
        counter_i = 1
        while counter_i < length_n:
            key_value = arr[counter_i]
            key_comparable = dict_alpha[key_value]
            counter_j = counter_i - 1

            while True:
                if counter_j < 0:
                    break
                if dict_alpha[arr[counter_j]] > key_comparable:
                    arr[counter_j + 1] = arr[counter_j]
                    counter_j -= 1
                else:
                    break

            arr[counter_j + 1] = key_value
            counter_i += 1

    insertion_sort(words_list, len(words_list))

    result_string: str = ''
    pos_i: int = 0
    length_words: int = len(words_list)
    while pos_i < length_words:
        result_string += words_list[pos_i]
        if pos_i != length_words - 1:
            result_string += ' '
        pos_i += 1

    return result_string