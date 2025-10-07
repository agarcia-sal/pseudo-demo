from typing import List


def sort_numbers(input_str: str) -> str:
    mapping: dict[str, int] = {
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

    def comparator(a: str, b: str) -> bool:
        return mapping[a] < mapping[b]

    def quicksort(arr: List[str], left: int, right: int) -> None:
        if left >= right:
            return
        pivot_index = left
        low, high = left + 1, right

        while low <= high:
            while low <= right and comparator(arr[low], arr[pivot_index]):
                low += 1
            while high > left and not comparator(arr[high], arr[pivot_index]):
                high -= 1
            if low < high:
                arr[low], arr[high] = arr[high], arr[low]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        quicksort(arr, left, high - 1)
        quicksort(arr, high + 1, right)

    tokens = [token for token in input_str.split(' ') if token != '']

    if not tokens:
        return ''

    quicksort(tokens, 0, len(tokens) - 1)

    result = ''
    for word in tokens:
        if len(result) == 0:
            result = word
        else:
            result += ' ' + word

    return result