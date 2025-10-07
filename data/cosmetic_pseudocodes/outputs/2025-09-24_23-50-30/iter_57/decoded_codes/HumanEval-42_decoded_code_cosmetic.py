from typing import List

def incr_list(array_parameter: List[int]) -> List[int]:
    output_collection: List[int] = []
    idx: int = 0
    while idx < len(array_parameter):
        output_collection.append(array_parameter[idx] + 1)
        idx += 1
    return output_collection