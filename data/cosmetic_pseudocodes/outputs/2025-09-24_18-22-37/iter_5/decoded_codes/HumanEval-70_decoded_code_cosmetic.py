from typing import List


def strange_sort_list(collection_of_ints: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_flag: bool = False

    while collection_of_ints:
        if not toggle_flag:
            smallest_element: int = collection_of_ints[0]
            for idx in range(1, len(collection_of_ints)):
                if collection_of_ints[idx] < smallest_element:
                    smallest_element = collection_of_ints[idx]
            output_sequence.append(smallest_element)
            element_to_remove = smallest_element
        else:
            largest_element: int = collection_of_ints[0]
            for idx in range(1, len(collection_of_ints)):
                if collection_of_ints[idx] > largest_element:
                    largest_element = collection_of_ints[idx]
            output_sequence.append(largest_element)
            element_to_remove = largest_element

        for pos in range(len(collection_of_ints)):
            if collection_of_ints[pos] == element_to_remove:
                del collection_of_ints[pos]
                break

        toggle_flag = not toggle_flag

    return output_sequence