from typing import Iterable, List

def incr_list(collection_input: Iterable[int]) -> List[int]:
    result: List[int] = []
    index_counter: int = 0
    input_list = list(collection_input)  # Ensure indexing and length operations
    while index_counter < len(input_list):
        current_element = input_list[index_counter]
        result.append(current_element + 1)
        index_counter += 1
    return result