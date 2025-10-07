from typing import List, Optional, Callable

def sort_numbers(s: str) -> str:
    word_to_num: dict[str, int] = {
        'nine': 9, 'two': 2, 'seven': 7, 'one': 1,
        'three': 3, 'six': 6, 'four': 4, 'zero': 0,
        'five': 5, 'eight': 8
    }

    # Split input string by spaces, trim each piece, and filter out empty strings
    def trimmed_filtered_split(text: str) -> List[str]:
        parts = text.split(' ')
        trimmed = [(x if x.strip() != '' else None) for x in parts]
        return [x for x in trimmed if x is not None]

    values: List[str] = trimmed_filtered_split(s)

    def recur_sort(arr: List[str], i: int) -> List[str]:
        if i >= len(arr):
            return arr

        def recurse_loop(lst: List[str], j: int) -> List[str]:
            if j < len(arr) - i - 1:
                if word_to_num[lst[j]] > word_to_num[lst[j + 1]]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap
                return recurse_loop(lst, j + 1)
            else:
                return lst

        return recur_sort(recurse_loop(arr, 0), i + 1)

    sorted_values: List[str] = recur_sort(values, 0)

    # foldl with accumulator starting as empty string, adding each element with a preceding space,
    # then slice off the first space
    result: str = ''.join(' ' + cur for cur in sorted_values)[1:] if sorted_values else ''

    return result