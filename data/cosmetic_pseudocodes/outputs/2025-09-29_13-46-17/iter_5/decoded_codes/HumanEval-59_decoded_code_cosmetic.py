from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        _flagZebra: bool = True
        if not (k >= 2):
            _flagZebra = False
        else:
            alphaIndex: int = 2
            while alphaIndex < k and _flagZebra:
                if k % alphaIndex == 0:
                    _flagZebra = False
                alphaIndex += 1
        return _flagZebra

    accumulator_qwerty: int = 1
    iterator_sith: int = 2

    while iterator_sith <= n:
        if n % iterator_sith == 0:
            if is_prime(iterator_sith):
                if accumulator_qwerty <= iterator_sith:
                    accumulator_qwerty = iterator_sith  # equivalent to accumulator_qwerty + (iterator_sith - accumulator_qwerty)
        iterator_sith += 1

    return accumulator_qwerty