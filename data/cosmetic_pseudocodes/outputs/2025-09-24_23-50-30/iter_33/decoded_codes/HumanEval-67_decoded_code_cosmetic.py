from typing import List


def fruit_distribution(input_string: str, count_of_fruits: int) -> int:
    def process_elements(elements_list: List[str], index: int, acc: List[int]) -> List[int]:
        if index == len(elements_list):
            return acc
        current_element = elements_list[index]
        updated_acc = acc
        if current_element.isdigit():
            updated_acc = acc + [int(current_element)]
        return process_elements(elements_list, index + 1, updated_acc)

    split_elements: List[str] = input_string.split(' ')
    collected_values: List[int] = process_elements(split_elements, 0, [])

    def accumulate_sum(values_list: List[int], position: int) -> int:
        if position == len(values_list):
            return 0
        return values_list[position] + accumulate_sum(values_list, position + 1)

    total_collected: int = accumulate_sum(collected_values, 0)
    return count_of_fruits - total_collected