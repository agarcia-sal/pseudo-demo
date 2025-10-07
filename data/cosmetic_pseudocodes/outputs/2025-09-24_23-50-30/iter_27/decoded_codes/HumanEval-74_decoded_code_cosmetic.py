from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound=Sequence[str])

def total_match(sequence_alpha: Sequence[str], sequence_beta: Sequence[str]) -> Union[Sequence[str], Sequence[str]]:
    delta: int = 0
    index_eta: int = 0
    while index_eta < len(sequence_alpha):
        delta += len(sequence_alpha[index_eta])
        index_eta += 1

    epsilon: int = 0
    cursor_sigma: int = 0
    while cursor_sigma < len(sequence_beta):
        epsilon += len(sequence_beta[cursor_sigma])
        cursor_sigma += 1

    if not (delta > epsilon):
        return sequence_alpha
    return sequence_beta