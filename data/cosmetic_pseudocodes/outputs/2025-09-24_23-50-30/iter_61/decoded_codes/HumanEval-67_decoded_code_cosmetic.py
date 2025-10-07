from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def helper(list_items: List[str], counter: int, acc: List[int]) -> List[int]:
        while counter < len(list_items):
            if not list_items[counter].isdigit():
                counter += 1
            else:
                acc.append(int(list_items[counter]))
                counter += 1
        return acc

    list_items = string_description.split()
    list_of_numbers = helper(list_items, 0, [])
    total_sum = 0
    index = 0
    while index < len(list_of_numbers):
        total_sum += list_of_numbers[index]
        index += 1
    return total_number_of_fruits - total_sum