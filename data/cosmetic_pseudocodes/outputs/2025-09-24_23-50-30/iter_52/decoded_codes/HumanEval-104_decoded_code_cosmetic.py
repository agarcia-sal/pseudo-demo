from typing import List, Iterable


def unique_digits(input_collection: Iterable[int]) -> List[int]:
    def digits_all_odd(number: int) -> bool:
        def check_odd_digits(index: int, digit_list: List[int]) -> bool:
            if index == len(digit_list):
                return True
            if digit_list[index] % 2 == 0:
                return False
            return check_odd_digits(index + 1, digit_list)

        digit_array: List[int] = []
        temp_num = number
        while temp_num > 0:
            digit_array = [temp_num % 10] + digit_array
            temp_num //= 10

        # If number is 0, digit_array is empty and should treat as not all odd digits
        if not digit_array:
            return False

        return check_odd_digits(0, digit_array)

    def filter_odds(collection: Iterable[int], acc: List[int], idx: int) -> List[int]:
        coll_list = list(collection)
        if idx == len(coll_list):
            return acc
        if digits_all_odd(coll_list[idx]):
            acc = acc + [coll_list[idx]]
        return filter_odds(coll_list, acc, idx + 1)

    filtered_elements = filter_odds(input_collection, [], 0)

    def insertion_sort(arr: List[int], n: int) -> None:
        if n <= 1:
            return
        insertion_sort(arr, n - 1)
        key = arr[n - 1]
        j = n - 2
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    insertion_sort(filtered_elements, len(filtered_elements))

    return filtered_elements