from typing import TypeVar, List, Sequence

T = TypeVar('T')

def unique(list_of_elements: Sequence[T]) -> List[T]:
    def helper(input_collection: Sequence[T], output_collection: List[T], input_index: int) -> List[T]:
        if input_index >= len(input_collection):
            return output_collection
        current_item = input_collection[input_index]
        if current_item not in output_collection:
            output_collection.append(current_item)
        return helper(input_collection, output_collection, input_index + 1)

    temp_list = helper(list_of_elements, [], 0)
    sorted_list = sorted(temp_list)
    return sorted_list