from typing import Sequence, TypeVar, Sized

T = TypeVar('T', bound=Sized)

def total_match(alpha_collection: Sequence[T], beta_collection: Sequence[T]) -> Sequence[T]:
    def accumulate_length(collection: Sequence[T], index: int, accumulator: int) -> int:
        if not (index < len(collection)):
            return accumulator
        else:
            return accumulate_length(collection, index + 1, accumulator + len(collection[index]))
    first_total_length = accumulate_length(alpha_collection, 0, 0)
    second_total_length = accumulate_length(beta_collection, 0, 0)
    if first_total_length <= second_total_length:
        return alpha_collection
    else:
        return beta_collection