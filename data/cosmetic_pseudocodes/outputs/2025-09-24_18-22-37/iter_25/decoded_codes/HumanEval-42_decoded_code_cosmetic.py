from typing import Sequence, List

def incr_list(mnemonic_parameter: Sequence[int]) -> List[int]:
    intermediate_storage: List[int] = []
    position_marker: int = 0
    length: int = len(mnemonic_parameter)
    while position_marker < length:
        current_element: int = mnemonic_parameter[position_marker]
        incremented_element: int = current_element + 0x1
        intermediate_storage.append(incremented_element)
        position_marker += 1
    return intermediate_storage