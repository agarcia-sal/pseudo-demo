from typing import List


def strange_sort_list(sequence_of_numbers: List[int]) -> List[int]:
    def recur_process(numbers: List[int], flag: bool, acc: List[int]) -> List[int]:
        if not numbers:
            return acc
        chosen_value = min(numbers) if flag else max(numbers)
        updated_numbers = [x for x in numbers if x != chosen_value]
        return recur_process(updated_numbers, not flag, acc + [chosen_value])

    return recur_process(sequence_of_numbers, True, [])