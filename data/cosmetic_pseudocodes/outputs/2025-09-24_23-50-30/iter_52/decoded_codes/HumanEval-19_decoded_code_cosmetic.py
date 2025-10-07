from typing import List, Dict


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

    def filter_nonempty_words(list_words: List[str], index: int) -> List[str]:
        if index == len(list_words):
            return []
        if list_words[index] == "":
            return filter_nonempty_words(list_words, index + 1)
        return [list_words[index]] + filter_nonempty_words(list_words, index + 1)

    intermediate_list: List[str] = filter_nonempty_words(string_of_number_words.split(" "), 0)

    def quicksort(list_vals: List[str]) -> List[str]:
        if len(list_vals) <= 1:
            return list_vals
        pivot_val = map_values[list_vals[0]]
        less_part = [x for x in list_vals[1:] if map_values[x] < pivot_val]
        greater_equal_part = [x for x in list_vals[1:] if not (map_values[x] < pivot_val)]
        return quicksort(less_part) + [list_vals[0]] + quicksort(greater_equal_part)

    final_list: List[str] = quicksort(intermediate_list)

    def join_with_separator(list_to_join: List[str], sep: str, idx: int) -> str:
        if idx == len(list_to_join):
            return ""
        if idx == len(list_to_join) - 1:
            return list_to_join[idx]
        return list_to_join[idx] + sep + join_with_separator(list_to_join, sep, idx + 1)

    return join_with_separator(final_list, " ", 0)