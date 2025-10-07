from typing import List

def sort_numbers(string_of_number_words: str) -> str:
    value_dictionary: dict[str, int] = {
        'nine': 9,
        'one': 1,
        'five': 5,
        'three': 3,
        'six': 6,
        'eight': 8,
        'two': 2,
        'zero': 0,
        'seven': 7,
        'four': 4
    }

    def recursive_filter(words_list: List[str], index: int, accumulator: List[str]) -> List[str]:
        if index >= len(words_list):
            return accumulator
        current_word = words_list[index]
        if current_word != '':
            accumulator.append(current_word)
        return recursive_filter(words_list, index + 1, accumulator)

    words_array: List[str] = string_of_number_words.split(' ')
    filtered_words: List[str] = recursive_filter(words_array, 0, [])

    def insertion_sort(arr: List[str], n: int) -> None:
        if n > 1:
            insertion_sort(arr, n - 1)
            key = arr[n - 1]
            key_val = value_dictionary[key]
            j = n - 2
            while j >= 0 and value_dictionary[arr[j]] > key_val:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    insertion_sort(filtered_words, len(filtered_words))

    return ' '.join(filtered_words)