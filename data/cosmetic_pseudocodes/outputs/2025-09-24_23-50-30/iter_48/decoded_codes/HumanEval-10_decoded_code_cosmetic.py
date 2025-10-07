from typing import Sequence, TypeVar

T = TypeVar('T', bound=Sequence)


def is_palindrome(tau: T) -> bool:
    return tau == tau[::-1]


def make_palindrome(alpha: T) -> T:
    partition_index = 0
    min_index = len(alpha)
    if min_index != 0:
        while True:
            if not is_palindrome(alpha[partition_index:min_index]):
                partition_index += 1
            else:
                break
    return alpha + alpha[:partition_index][::-1]