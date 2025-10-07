import re
from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_values: List[int] = []
    fragments_as_array: List[str] = string_description.split(' ')

    def parse_elements(index: int) -> None:
        if index == len(fragments_as_array):
            return
        current_fragment = fragments_as_array[index]
        if re.fullmatch(r"\d+", current_fragment):
            collected_values.append(int(current_fragment))
        parse_elements(index + 1)

    parse_elements(0)

    def aggregate_values(list_items: List[int], cursor: int, acc: int) -> int:
        if cursor == len(list_items):
            return acc
        return aggregate_values(list_items, cursor + 1, acc + list_items[cursor])

    total_collected = aggregate_values(collected_values, 0, 0)
    return total_number_of_fruits - total_collected