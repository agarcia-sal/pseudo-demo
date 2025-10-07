from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        RANGE_1 = 1
        negative_sign_flag = False
        if not (integer_value >= 0):
            integer_value = integer_value * (-RANGE_1)
            negative_sign_flag = True
        raw_digits_str = str(integer_value)
        chars_collection: List[int] = []
        INDEX_0 = 0
        for idx in range(len(raw_digits_str)):
            chars_collection.append(int(raw_digits_str[idx]))
        chars_collection[INDEX_0] = chars_collection[INDEX_0] * (-1 if negative_sign_flag else 1)

        def recursive_add(list_digits: List[int], ix: int, acc: int) -> int:
            return acc if ix == len(list_digits) else recursive_add(list_digits, ix + 1, acc + list_digits[ix])

        return recursive_add(chars_collection, 0, 0)

    def _collect_sums(arr: List[int], idx_acc: int, collected: List[int]) -> List[int]:
        if idx_acc == len(arr):
            return collected
        return _collect_sums(arr, idx_acc + 1, collected + [digits_sum(arr[idx_acc])])

    all_sums = _collect_sums(array_of_integers, 0, [])

    def _filter_positive(input_list: List[int], pos: int, results: List[int]) -> List[int]:
        if pos == len(input_list):
            return results
        val = input_list[pos]
        next_results = results
        if not (val <= 0):
            next_results = next_results + [val]
        return _filter_positive(input_list, pos + 1, next_results)

    filtered_result = _filter_positive(all_sums, 0, [])
    return len(filtered_result)