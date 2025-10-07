from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def gather_if_all_odd(original_list: List[int], filtered_container: List[int]) -> None:
        position: int = 0
        while position < len(original_list):
            current = original_list[position]
            bit_collection = [int(d) for d in str(current)]
            has_even = False
            pointer = 0
            # iterate through digits until even found or end reached
            while pointer < len(bit_collection) and not has_even:
                if bit_collection[pointer] % 2 == 0:
                    has_even = True
                pointer += 1
            if not has_even:
                filtered_container.append(current)
            position += 1

    result_container: List[int] = []
    gather_if_all_odd(list_of_positive_integers, result_container)

    def insertion_sort(arr: List[int]) -> None:
        k = 1
        while k < len(arr):
            comp = arr[k]
            j = k - 1
            while j >= 0 and arr[j] > comp:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = comp
            k += 1

    insertion_sort(result_container)
    return result_container