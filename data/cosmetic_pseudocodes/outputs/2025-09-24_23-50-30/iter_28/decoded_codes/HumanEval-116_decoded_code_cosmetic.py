from typing import List, Callable


def sort_array(input_list: List[int]) -> List[int]:
    def count_ones(binary_string: str) -> int:
        acc = 0
        idx = 1  # Start from index 1 as in pseudocode
        while idx < len(binary_string):
            if binary_string[idx] == '1':
                acc += 1
            idx += 1
        return acc

    def binary_repr(number: int) -> str:
        return bin(number)

    def bubble_sort_asc(list_ref: List[int]) -> None:
        n = len(list_ref)
        a = 0
        while a < n - 1:
            b = 0
            while b < n - a - 1:
                if not (list_ref[b] <= list_ref[b + 1]):
                    list_ref[b], list_ref[b + 1] = list_ref[b + 1], list_ref[b]
                b += 1
            a += 1

    fresh_array = []
    for each_elem in input_list:
        fresh_array.append(each_elem)

    bubble_sort_asc(fresh_array)

    def helper(a: int, c: int) -> int:
        return count_ones(binary_repr(c))

    def insertion_sort_by_key(arr: List[int], key_func: Callable[[int], int]) -> None:
        for i in range(1, len(arr)):
            curr_val = arr[i]
            curr_key = key_func(arr[i])
            j = i - 1
            while j >= 0 and not (key_func(arr[j]) <= curr_key):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = curr_val

    insertion_sort_by_key(fresh_array, helper)

    return fresh_array