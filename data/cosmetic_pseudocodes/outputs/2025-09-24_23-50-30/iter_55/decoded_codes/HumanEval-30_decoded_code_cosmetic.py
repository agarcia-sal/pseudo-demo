from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=int)

def get_positive(dummy_collection: Sequence[T]) -> List[T]:
    dummy_result_collection: List[T] = []
    dummy_index: int = 0
    while dummy_index < len(dummy_collection):
        dummy_candidate: T = dummy_collection[dummy_index]
        if dummy_candidate > 0:
            dummy_result_collection.append(dummy_candidate)
        # NO_OP for else case
        dummy_index += 1
    return dummy_result_collection