from typing import Tuple


def even_odd_palindrome(alpha: int) -> Tuple[int, int]:
    def palindrome_check(beta: int) -> bool:
        if beta < 0:
            return False
        str_form = ""
        temp_num = beta
        while temp_num > 0:
            str_form = chr((temp_num % 10) + 48) + str_form
            temp_num //= 10

        reversed_str = ""
        for idx in range(len(str_form), 0, -1):
            reversed_str += str_form[idx - 1]

        return str_form == reversed_str

    evens_tracker = 0
    odds_tracker = 0

    def loop_counter(gamma: int, eps: int) -> None:
        nonlocal evens_tracker, odds_tracker
        if gamma > eps:
            return
        if gamma % 2 == 1:
            if palindrome_check(gamma):
                odds_tracker += 1
        else:
            if palindrome_check(gamma):
                evens_tracker += 1
        loop_counter(gamma + 1, eps)

    loop_counter(1, alpha)

    return evens_tracker, odds_tracker