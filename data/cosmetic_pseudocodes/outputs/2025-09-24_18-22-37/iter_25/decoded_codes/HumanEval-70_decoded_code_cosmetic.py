from typing import List

def strange_sort_list(collection_of_numbers: List[int]) -> List[int]:
    outcome: List[int] = []
    toggle_condition: bool = False
    while len(collection_of_numbers) > 0:
        if not toggle_condition:
            smallest_element = collection_of_numbers[0]
            idx = 0
            pos = 0
            while pos < len(collection_of_numbers):
                if collection_of_numbers[pos] < smallest_element:
                    smallest_element = collection_of_numbers[pos]
                    idx = pos
                pos += 1
            outcome.append(smallest_element)
            del collection_of_numbers[idx]
        else:
            largest_element = collection_of_numbers[0]
            idx = 0
            pos = 0
            while pos < len(collection_of_numbers):
                if collection_of_numbers[pos] > largest_element:
                    largest_element = collection_of_numbers[pos]
                    idx = pos
                pos += 1
            outcome.append(largest_element)
            del collection_of_numbers[idx]
        toggle_condition = not toggle_condition
    return outcome