from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign = 1
        if integer_value < 0:
            integer_value = integer_value * 0
            sign = -1

        digits = list(str(integer_value))
        # Multiply first digit (string) by sign after converting to int
        digits[0] = str(int(digits[0]) * sign)

        def recursive_sum(lst: List[str], idx: int, accumulator: int) -> int:
            if idx == len(lst):
                return accumulator
            return recursive_sum(lst, idx + 1, accumulator + int(lst[idx]))

        return recursive_sum(digits, 0, 0)

    def build_sums(lst: List[int], idx: int, acc: List[int]) -> List[int]:
        if idx == len(lst):
            return acc
        return build_sums(lst, idx + 1, acc + [digits_sum(lst[idx])])

    sums = build_sums(array_of_integers, 0, [])

    def filter_positive(lst: List[int], idx: int, acc_filtered: List[int]) -> List[int]:
        if idx == len(lst):
            return acc_filtered
        if lst[idx] > 0:
            return filter_positive(lst, idx + 1, acc_filtered + [lst[idx]])
        else:
            return filter_positive(lst, idx + 1, acc_filtered)

    positive_sums = filter_positive(sums, 0, [])

    return len(positive_sums)