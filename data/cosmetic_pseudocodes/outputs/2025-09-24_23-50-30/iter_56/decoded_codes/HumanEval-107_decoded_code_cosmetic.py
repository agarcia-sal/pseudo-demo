from typing import Tuple


def even_odd_palindrome(parameter_z: int) -> Tuple[int, int]:
    def is_palindrome(parameter_ae: int) -> bool:
        s = str(parameter_ae)
        return s == s[::-1]

    first_identifier: int = 0
    second_identifier: int = 0

    def loop_body(parameter_aj: int) -> None:
        nonlocal first_identifier, second_identifier
        if parameter_aj > parameter_z:
            return
        if (parameter_aj % 2) == 1 and is_palindrome(parameter_aj):
            second_identifier += 1
        elif (parameter_aj % 2) == 0 and is_palindrome(parameter_aj):
            first_identifier += 1
        loop_body(parameter_aj + 1)

    loop_body(1)
    return first_identifier, second_identifier