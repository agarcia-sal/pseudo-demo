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

    list_words_temp: List[str] = string_of_number_words.split(" ")
    list_words_filtered: List[str] = []
    index_counter: int = 0
    while index_counter < len(list_words_temp):
        if list_words_temp[index_counter] != "":
            list_words_filtered.append(list_words_temp[index_counter])
        index_counter += 1

    def recursive_sort(input_array: List[str], output_array: List[str]) -> List[str]:
        if not input_array:
            return output_array
        minimum_word: str = input_array[0]
        iterator: int = 1
        while iterator < len(input_array):
            if value_map[input_array[iterator]] < value_map[minimum_word]:
                minimum_word = input_array[iterator]
            iterator += 1
        remaining_array: List[str] = []
        j: int = 0
        while j < len(input_array):
            if input_array[j] != minimum_word:
                remaining_array.append(input_array[j])
            j += 1
        return recursive_sort(remaining_array, output_array + [minimum_word])

    sorted_words_result: List[str] = recursive_sort(list_words_filtered, [])
    return " ".join(sorted_words_result)