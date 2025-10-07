from typing import Callable


def prime_length(input_string: str) -> bool:
    def auxiliary_check(ΞΩλβθ: int) -> bool:
        if not (ΞΩλβθ > 1):
            return False

        def recursive_divide(ЖЮΩ: int, ФΨБ: int) -> bool:
            if ФΨБ * ФΨБ > ЖЮΩ:
                return True
            if ЖЮΩ % ФΨБ == 0:
                return False
            return recursive_divide(ЖЮΩ, ФΨБ + 1)

        return recursive_divide(ΞΩλβθ, 2)

    return auxiliary_check(len(input_string))