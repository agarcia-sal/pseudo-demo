from typing import List


def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    def process(input_sequence: List[int], accumulator: List[int], flag: bool) -> List[int]:
        if not input_sequence:
            return accumulator
        if flag:
            selected_element = min(input_sequence)
        else:
            selected_element = max(input_sequence)

        # Remove only one occurrence of selected_element from input_sequence
        removed_once = False
        filtered_sequence = []
        for x in input_sequence:
            if x == selected_element and not removed_once:
                removed_once = True
                continue
            filtered_sequence.append(x)

        return process(filtered_sequence, accumulator + [selected_element], not flag)

    return process(array_of_numbers, [], True)