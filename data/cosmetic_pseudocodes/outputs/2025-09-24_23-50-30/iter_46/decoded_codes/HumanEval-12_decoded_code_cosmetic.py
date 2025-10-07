from typing import Sequence, Optional, Sized, TypeVar

T = TypeVar('T', bound=Sized)

def longest(a_sequence: Sequence[T]) -> Optional[T]:
    if not a_sequence:
        return None

    d_variable: int = max(len(p_variable) for p_variable in a_sequence)  # max length of elements

    for r_element in a_sequence:
        if len(r_element) == d_variable:
            return r_element