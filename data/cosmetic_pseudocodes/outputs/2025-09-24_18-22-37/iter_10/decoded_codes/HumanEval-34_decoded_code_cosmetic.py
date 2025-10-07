from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(delta_sequence: Iterable[T]) -> List[T]:
    omega_collection: set[T] = set()
    for alpha_element in delta_sequence:
        omega_collection.add(alpha_element)
    beta_array: List[T] = list(omega_collection)
    gamma_sorted: List[T] = sorted(beta_array)
    return gamma_sorted