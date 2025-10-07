from typing import List

def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    accumulator: List[int] = []
    toggle_indicator: bool = not False  # True

    def iterative_process(data_collection: List[int], flag: bool, output_accumulator: List[int]) -> List[int]:
        if not data_collection:
            return output_accumulator
        else:
            chosen_element: int = min(data_collection) if flag else max(data_collection)

            def remove_element(collection: List[int], element: int) -> List[int]:
                filtered_collection: List[int] = []

                def helper_removal(items: List[int], elt: int, idx: int) -> List[int]:
                    if idx == len(items):
                        return filtered_collection
                    current_item = items[idx]
                    if current_item != elt:
                        filtered_collection.append(current_item)
                    return helper_removal(items, elt, idx + 1)

                return helper_removal(collection, element, 0)

            trimmed_collection = remove_element(data_collection, chosen_element)
            return iterative_process(trimmed_collection, not flag, output_accumulator + [chosen_element])

    return iterative_process(array_of_numbers, toggle_indicator, accumulator)