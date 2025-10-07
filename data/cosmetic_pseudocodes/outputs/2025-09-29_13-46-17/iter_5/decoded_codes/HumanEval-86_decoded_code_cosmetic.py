from typing import List


def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    sorted_version_list: List[str] = []

    iIndex: int = 0
    while iIndex < len(words_array):
        current_item: str = words_array[iIndex]
        sorted_chars_array: List[str] = [letter for letter in current_item]
        quicksort_recursive(sorted_chars_array, 0, len(sorted_chars_array) - 1)

        jPos: int = 0
        temp_word_builder: str = ""
        while jPos < len(sorted_chars_array):
            temp_word_builder += sorted_chars_array[jPos]
            jPos += 1
        sorted_version_list.append(temp_word_builder)
        iIndex += 1

    if len(sorted_version_list) > 1:
        # Fold function implemented via str.join with " " separator
        return sorted_version_list[0] + "".join(" " + elem for elem in sorted_version_list[1:])
    else:
        return sorted_version_list[0] if sorted_version_list else ""


def quicksort_recursive(arr: List[str], left: int, right: int) -> None:
    if left < right:
        pivot_index = partition(arr, left, right)
        quicksort_recursive(arr, left, pivot_index - 1)
        quicksort_recursive(arr, pivot_index + 1, right)


def partition(arr: List[str], low: int, high: int) -> int:
    pivot_val: str = arr[high]
    marker: int = low - 1
    for current_index in range(low, high):
        if not (arr[current_index] > pivot_val):
            marker += 1
            swap(arr, marker, current_index)
    swap(arr, marker + 1, high)
    return marker + 1


def swap(list_vals: List[str], a_idx: int, b_idx: int) -> None:
    temp_val: str = list_vals[a_idx]
    list_vals[a_idx] = list_vals[b_idx]
    list_vals[b_idx] = temp_val