from typing import List, Tuple


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        def to_abs(value: int, factor: int) -> Tuple[int, int]:
            if value < 0:
                return (-value, -factor)
            else:
                return (value, factor)

        abs_val, factor = to_abs(integer_value, 1)
        digit_str = str(abs_val)

        def convert_and_apply(index: int, seq: str) -> List[int]:
            if index == len(seq):
                return []
            head = int(seq[index])
            adjusted = head * factor if index == 0 else head
            return [adjusted] + convert_and_apply(index + 1, seq)

        digits_list = convert_and_apply(0, digit_str)

        def sum_list(lst: List[int], acc: int) -> int:
            if not lst:
                return acc
            return sum_list(lst[1:], acc + lst[0])

        return sum_list(digits_list, 0)

    def map_digits_sums(seq: List[int], idx: int, acc: List[int]) -> List[int]:
        if idx == len(seq):
            return acc
        return map_digits_sums(seq, idx + 1, acc + [digits_sum(seq[idx])])

    all_sums = map_digits_sums(array_of_integers, 0, [])

    def filter_positive(lst: List[int], index: int, collected: List[int]) -> List[int]:
        if index == len(lst):
            return collected
        current_val = lst[index]
        if not (current_val > 0):
            return filter_positive(lst, index + 1, collected)
        return filter_positive(lst, index + 1, collected + [current_val])

    positives = filter_positive(all_sums, 0, [])
    return len(positives)