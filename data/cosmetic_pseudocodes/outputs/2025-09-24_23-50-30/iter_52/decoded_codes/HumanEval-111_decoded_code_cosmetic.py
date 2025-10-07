from typing import List, Dict

def histogram(input_string: str) -> Dict[str, int]:
    def find_maximum_value(collection: List[str], current_index: int, current_max: int) -> int:
        if current_index >= len(collection):
            return current_max
        current_element = collection[current_index]
        element_count = collection.count(current_element)
        if element_count > current_max and current_element != "":
            return find_maximum_value(collection, current_index + 1, element_count)
        else:
            return find_maximum_value(collection, current_index + 1, current_max)

    def filter_by_max(collection: List[str], maximum: int, current_index: int, accumulator: Dict[str, int]) -> Dict[str, int]:
        if current_index >= len(collection):
            return accumulator
        candidate = collection[current_index]
        candidate_count = collection.count(candidate)
        if candidate_count == maximum:
            accumulator[candidate] = maximum
        return filter_by_max(collection, maximum, current_index + 1, accumulator)

    elements_list = input_string.split(" ")
    max_frequency = find_maximum_value(elements_list, 0, 0)
    result_mapping: Dict[str, int] = {}
    if max_frequency > 0:
        result_mapping = filter_by_max(elements_list, max_frequency, 0, {})
    return result_mapping