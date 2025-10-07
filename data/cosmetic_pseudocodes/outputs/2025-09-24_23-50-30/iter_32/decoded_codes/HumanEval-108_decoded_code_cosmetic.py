from typing import List


def count_nums(inputs: List[int]) -> int:
    def digits_sum(value: int) -> int:
        modifier = 1
        if value < 0:
            value = -value
            modifier = -1
        char_array = list(str(value))
        num_array = [int(ch) for ch in char_array]
        num_array[0] *= modifier
        index_counter = 0

        def sum_accumulator(accumulator: int) -> int:
            nonlocal index_counter
            if index_counter >= len(num_array):
                return accumulator
            accumulator += num_array[index_counter]
            index_counter += 1
            return sum_accumulator(accumulator)

        return sum_accumulator(0)

    temp_list: List[int] = []
    idx = 0
    while idx < len(inputs):
        current_value = inputs[idx]
        summed_value = digits_sum(current_value)
        temp_list.append(summed_value)
        idx += 1

    def filter_positive(lst: List[int], pos: int, result: List[int]) -> List[int]:
        if pos >= len(lst):
            return result
        if lst[pos] > 0:
            result.append(lst[pos])
        return filter_positive(lst, pos + 1, result)

    positives = filter_positive(temp_list, 0, [])
    return len(positives)