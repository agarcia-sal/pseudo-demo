from typing import List

def specialFilter(list_of_numbers: List[int]) -> int:
    def count_accumulator(accum_count: int, num_list: List[int], current_index: int) -> int:
        if current_index >= len(num_list):
            return accum_count

        element = num_list[current_index]
        odd_set = {9, 3, 1, 7, 5}
        sprite = str(element)
        head_digit = int(sprite[0])
        tail_digit = int(sprite[-1])

        if element <= 10:
            return count_accumulator(accum_count, num_list, current_index + 1)
        if head_digit not in odd_set:
            return count_accumulator(accum_count, num_list, current_index + 1)
        if tail_digit not in odd_set:
            return count_accumulator(accum_count, num_list, current_index + 1)

        updated_count = accum_count + 1
        return count_accumulator(updated_count, num_list, current_index + 1)

    return count_accumulator(0, list_of_numbers, 0)