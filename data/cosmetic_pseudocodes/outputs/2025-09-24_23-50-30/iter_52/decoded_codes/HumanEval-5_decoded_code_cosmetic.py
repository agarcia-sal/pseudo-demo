from typing import Sequence, TypeVar, List, Union

T = TypeVar("T")
U = TypeVar("U")

def intersperse(sequence_alpha: Sequence[T], symbol_beta: U) -> List[Union[T, U]]:
    def helper(index_gamma: int) -> List[Union[T, U]]:
        if index_gamma == len(sequence_alpha) - 1:
            return [sequence_alpha[index_gamma]]
        else:
            return [sequence_alpha[index_gamma], symbol_beta] + helper(index_gamma + 1)

    if len(sequence_alpha) == 0:
        return []
    else:
        return helper(0)