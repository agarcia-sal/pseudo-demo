from typing import List

def sorted_list_sum(input_strings: List[str]) -> List[str]:
    ordered_collection: List[str] = sorted(input_strings)
    filtered_accumulator: List[str] = []
    indexer: int = 0
    while True:
        if indexer >= len(ordered_collection):
            break
        current_candidate: str = ordered_collection[indexer]
        if len(current_candidate) % 2 == 0:
            filtered_accumulator.append(current_candidate)
        indexer += 1
    final_output: List[str] = sorted(filtered_accumulator, key=len)
    return final_output