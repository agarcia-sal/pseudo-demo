from typing import Sequence, TypeVar, List

T = TypeVar('T')
U = TypeVar('U')


def intersperse(alpha_sequence: Sequence[T], beta_marker: U) -> List[object]:
    omega_accumulator: List[object] = []
    if not alpha_sequence:
        return omega_accumulator
    for idx in range(len(alpha_sequence) - 1):
        omega_accumulator.append(alpha_sequence[idx])
        omega_accumulator.append(beta_marker)
    omega_accumulator.append(alpha_sequence[-1])
    return omega_accumulator