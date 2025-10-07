from typing import List, Dict


def sort_numbers(string_of_number_words: str) -> str:
    mapping_table: Dict[str, int] = {
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

    def split_and_filter(input_string: str, index: int, acc: List[str]) -> List[str]:
        length = len(input_string)
        if index >= length:
            return acc
        current_word = []
        while index < length and input_string[index] != ' ':
            current_word.append(input_string[index])
            index += 1
        word = ''.join(current_word)
        if word:
            acc.append(word)
        while index < length and input_string[index] == ' ':
            index += 1
        return split_and_filter(input_string, index, acc)

    # The pseudocode starts at index=1 (1-based), Python is 0-based
    # Adapting accordingly by starting at index=0 to cover the full string
    temp_list = split_and_filter(string_of_number_words, 0, [])

    def quicksort(list_in: List[str]) -> List[str]:
        if len(list_in) <= 1:
            return list_in
        pivot = list_in[0]
        less_than_pivot: List[str] = []
        greater_equal_pivot: List[str] = []
        for element in list_in[1:]:
            if mapping_table[element] < mapping_table[pivot]:
                less_than_pivot.append(element)
            else:
                greater_equal_pivot.append(element)
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_equal_pivot)

    ordered_words = quicksort(temp_list)
    return ' '.join(ordered_words)