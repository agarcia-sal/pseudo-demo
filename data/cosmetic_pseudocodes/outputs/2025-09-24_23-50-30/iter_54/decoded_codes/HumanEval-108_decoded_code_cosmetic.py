from typing import List


def count_nums(input_array: List[int]) -> int:
    def digits_sum(value: int) -> int:
        factor = 1
        if value < 0:
            value = -value
            factor = -1

        digits = str(value)
        digit_values: List[int] = [int(d) for d in digits]
        digit_values[0] *= factor

        def sum_list(lst: List[int], acc: int) -> int:
            if not lst:
                return acc
            return sum_list(lst[1:], acc + lst[0])

        return sum_list(digit_values, 0)

    def collect_results(arr: List[int], idx: int, acc: List[int]) -> List[int]:
        if idx >= len(arr):
            return acc
        return collect_results(arr, idx + 1, acc + [digits_sum(arr[idx])])

    results = collect_results(input_array, 0, [])

    def filter_positive(l: List[int], acc: List[int]) -> List[int]:
        if not l:
            return acc
        x, *rest = l
        if x > 0:
            return filter_positive(rest, acc + [x])
        return filter_positive(rest, acc)

    positive_results = filter_positive(results, [])

    return len(positive_results)