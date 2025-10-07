from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    nums_collection: List[int] = []
    words_list: List[str] = string_description.split(' ')
    idx: int = 0

    while idx < len(words_list):
        current_item: str = words_list[idx]
        if "0" <= current_item <= "9":
            number_value: int = int(current_item)
            nums_collection.append(number_value)
        idx += 1

    total_sum: int = 0
    sum_index: int = 0
    while sum_index < len(nums_collection):
        total_sum += nums_collection[sum_index]
        sum_index += 1

    result: int = total_number_of_fruits - total_sum
    return result