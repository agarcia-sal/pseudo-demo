from typing import List, Dict


def sort_numbers(string_of_number_words: str) -> str:
    value_map: Dict[str, int] = {}
    value_map['zero'], value_map['one'], value_map['two'], value_map['three'], value_map['four'] = 0, 1, 2, 3, 4
    value_map['five'], value_map['six'], value_map['seven'], value_map['eight'], value_map['nine'] = 5, 6, 7, 8, 9

    def filter_nonempty(words_list: List[str], index: int, acc: List[str]) -> List[str]:
        if index >= len(words_list):
            return acc
        current_word = words_list[index]
        if len(current_word) > 0:
            return filter_nonempty(words_list, index + 1, acc + [current_word])
        else:
            return filter_nonempty(words_list, index + 1, acc)

    words_array = string_of_number_words.split(' ')
    filtered_words = filter_nonempty(words_array, 0, [])

    def insert_in_order(sorted_arr: List[str], element: str) -> List[str]:
        if len(sorted_arr) == 0:
            return [element]
        elif value_map[element] < value_map[sorted_arr[0]]:
            return [element] + sorted_arr
        else:
            return [sorted_arr[0]] + insert_in_order(sorted_arr[1:], element)

    def sort_recursive(unsorted_arr: List[str], acc: List[str]) -> List[str]:
        if len(unsorted_arr) == 0:
            return acc
        first_elem = unsorted_arr[0]
        remaining = unsorted_arr[1:]
        return sort_recursive(remaining, insert_in_order(acc, first_elem))

    sorted_list = sort_recursive(filtered_words, [])

    return ' '.join(sorted_list)