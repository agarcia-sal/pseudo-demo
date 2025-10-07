from typing import Any, List, Sequence

def filter_integers(aggregate_container: Sequence[Any]) -> List[int]:
    def helper(accumulator: List[int], remaining_elements: Sequence[Any]) -> List[int]:
        if not remaining_elements:
            return accumulator
        current_candidate = remaining_elements[0]
        updated_accumulator = accumulator + [current_candidate] if isinstance(current_candidate, int) else accumulator
        return helper(updated_accumulator, remaining_elements[1:])
    return helper([], aggregate_container)