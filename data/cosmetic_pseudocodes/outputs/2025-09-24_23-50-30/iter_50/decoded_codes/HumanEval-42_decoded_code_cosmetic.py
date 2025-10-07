from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    output_sequence: List[int] = []
    cursor: int = 0
    while cursor < len(list_of_elements):
        output_sequence.append(list_of_elements[cursor] + 1)
        cursor += 1
    return output_sequence