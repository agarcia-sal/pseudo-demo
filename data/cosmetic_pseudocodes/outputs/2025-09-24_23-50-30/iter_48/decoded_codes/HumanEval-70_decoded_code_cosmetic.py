from typing import List

def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_indicator: bool = False

    while array_of_numbers:
        if not toggle_indicator:
            candidate_element = array_of_numbers[0]
            for index in range(1, len(array_of_numbers)):
                if array_of_numbers[index] < candidate_element:
                    candidate_element = array_of_numbers[index]
        else:
            candidate_element = array_of_numbers[0]
            for index in range(1, len(array_of_numbers)):
                if array_of_numbers[index] > candidate_element:
                    candidate_element = array_of_numbers[index]

        output_sequence.append(candidate_element)
        temp_collection: List[int] = []

        found_candidate = False
        for item in array_of_numbers:
            # Include all items not equal to candidate_element
            # If item equals candidate_element, only include if already found one occurrence before
            if item != candidate_element or (item == candidate_element and found_candidate):
                temp_collection.append(item)
            elif item == candidate_element and not found_candidate:
                found_candidate = True

        array_of_numbers = temp_collection
        toggle_indicator = not toggle_indicator

    return output_sequence