from typing import Callable

def sort_numbers(string_of_number_words: str) -> str:
    digit_values: dict[str, int] = {
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
    temporary_list: list[str] = []
    split_words: list[str] = string_of_number_words.split(" ")
    for index in range(len(split_words)):
        candidate_word = split_words[index]
        if candidate_word != "":
            temporary_list.append(candidate_word)

    def comparator_function(a: str, b: str) -> bool:
        return digit_values[a] < digit_values[b]

    sorted_words_list: list[str] = sorted(temporary_list, key=lambda w: digit_values[w])

    concatenated_string = ""
    first_iteration = True
    for element in sorted_words_list:
        if first_iteration:
            concatenated_string = element
            first_iteration = False
        else:
            concatenated_string += " " + element
    return concatenated_string