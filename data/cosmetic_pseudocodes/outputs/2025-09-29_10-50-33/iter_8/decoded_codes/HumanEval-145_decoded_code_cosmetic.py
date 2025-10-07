from typing import List, Sequence


def order_by_points(sequence_of_values: Sequence[int]) -> List[int]:
    def digits_sum(value: int) -> int:
        def abs_adjustment(input_num: int, multiplier: int) -> int:
            if input_num < 0:
                input_num = -input_num
                multiplier = -multiplier
            return digits_extraction(input_num, multiplier)

        def digits_extraction(num: int, sign: int) -> int:
            digits_array: List[int] = []
            temp_num = num

            while temp_num > 0:
                digits_array.append(temp_num % 10)
                temp_num //= 10

            if digits_array:
                digits_array[0] *= sign
            else:
                digits_array.append(0)

            total_sum = 0
            idx = 0
            while True:
                if idx >= len(digits_array):
                    break
                total_sum += digits_array[idx]
                idx += 1

            return total_sum

        return abs_adjustment(value, 1)

    indexed_sequence: List[tuple[int, int]] = [(v, i) for i, v in enumerate(sequence_of_values)]

    def comparator(item_a: tuple[int, int], item_b: tuple[int, int]) -> int:
        sum_a = digits_sum(item_a[0])
        sum_b = digits_sum(item_b[0])
        if sum_a < sum_b:
            return -1
        if sum_a > sum_b:
            return 1
        return item_a[1] - item_b[1]

    # Sort using the comparator via key-function workaround
    from functools import cmp_to_key

    indexed_sequence.sort(key=cmp_to_key(comparator))

    sorted_values: List[int] = [pair[0] for pair in indexed_sequence]
    return sorted_values