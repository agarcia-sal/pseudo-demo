from typing import Sequence, TypeVar

T = TypeVar('T', bound=object)

def same_chars(container_alpha: Sequence[T], container_beta: Sequence[T]) -> bool:
    result_set_alpha: set[T] = set()
    result_set_beta: set[T] = set()
    index_alpha: int = 1
    index_beta: int = 1

    while not (index_alpha > len(container_alpha)):
        result_set_alpha |= {container_alpha[index_alpha - 1]}
        index_alpha += 1

    while not (index_beta > len(container_beta)):
        result_set_beta |= {container_beta[index_beta - 1]}
        index_beta += 1

    equality_flag: bool = False
    if not (result_set_alpha != result_set_beta):
        equality_flag = True

    return equality_flag