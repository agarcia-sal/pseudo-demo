from typing import List, Optional, TypeVar

T = TypeVar('T', bound=object)

def next_smallest(π𝞪𝛑𝛉: List[T]) -> Optional[T]:
    def ƀℵ₄(ξℷ: List[T]) -> Optional[T]:
        if len(ξℷ) < 2:
            return None
        # match ξℷ head :: tail
        # pattern match head : β𝛷, returns β𝛷 else None
        head, *tail = ξℷ
        return tail[0] if tail else None

    # Create sorted unique list preserving order within set of sorted π𝞪𝛑𝛉
    # Sort input
    sorted_list = sorted(π𝞪𝛑𝛉)
    # Unique elements in sorted order, fold: accumulate distinct elements preserving sorted order
    unique_sorted = []
    for x in sorted_list:
        if x not in unique_sorted:
            unique_sorted.append(x)

    # result from ƀℵ₄ on unique_sorted
    ΛɣϠ = ƀℵ₄(unique_sorted)
    return ΛɣϠ