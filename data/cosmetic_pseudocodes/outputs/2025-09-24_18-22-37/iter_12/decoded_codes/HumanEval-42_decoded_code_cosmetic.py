from typing import List

def incr_list(array_input: List[int]) -> List[int]:
    output_collection: List[int] = []
    idx: int = 0
    while idx < len(array_input):
        current_val: int = array_input[idx]
        incremented_val: int = current_val + 1
        output_collection.append(incremented_val)
        idx += 1
    return output_collection