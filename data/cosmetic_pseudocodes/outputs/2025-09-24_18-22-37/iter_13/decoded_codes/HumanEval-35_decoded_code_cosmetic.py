from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(input_sequence: Sequence[T]) -> T:
    if not input_sequence:
        raise ValueError("input_sequence must not be empty")
    pos: int = 1
    highest_value: T = input_sequence[0]
    while pos < len(input_sequence):
        current_item: T = input_sequence[pos]
        flag: bool
        if highest_value >= current_item:
            flag = True
        else:
            flag = False
        if flag is False:
            highest_value = current_item
            # break inside the switch-equivalent has no loop control effect; here, just continue
        # (cases TRUE and FALSE both break switch; loop continues except highest_value updated)
        pos += 1
    return highest_value