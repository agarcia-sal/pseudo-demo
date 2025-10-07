from typing import List


def sort_numbers(string_of_number_words: str) -> str:
    value_dictionary: dict[str, int] = {
        'nine': 9, 'eight': 8, 'seven': 7,
        'six': 6, 'five': 5, 'four': 4,
        'three': 3, 'two': 2, 'one': 1,
        'zero': 0
    }

    def recursive_filter(words: List[str], index: int, acc: List[str]) -> List[str]:
        if index >= len(words):
            return acc
        if words[index] == '':
            return recursive_filter(words, index + 1, acc)
        return recursive_filter(words, index + 1, acc + [words[index]])

    tokens: List[str] = recursive_filter(string_of_number_words.split(' '), 0, [])

    def insertion_sort(arr: List[str], n: int) -> None:
        if n <= 1:
            return
        insertion_sort(arr, n - 1)
        key_word = arr[n - 1]
        key_val = value_dictionary[key_word]
        j = n - 2
        while j >= 0 and value_dictionary[arr[j]] > key_val:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_word

    insertion_sort(tokens, len(tokens))

    result_string = ''
    for i in range(len(tokens)):
        if i == len(tokens) - 1:
            result_string += tokens[i]
        else:
            result_string += tokens[i] + ' '
    return result_string