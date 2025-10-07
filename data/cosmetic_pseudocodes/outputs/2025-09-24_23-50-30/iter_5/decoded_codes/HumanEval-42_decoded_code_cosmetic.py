from typing import List, Sequence

def incr_list(input_collection: Sequence[int]) -> List[int]:
    index: int = 0
    output_collection: List[int] = []

    while index < len(input_collection):
        output_collection.append(input_collection[index] + 1)
        index += 1

    return output_collection