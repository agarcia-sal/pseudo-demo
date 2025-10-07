from typing import Tuple


def even_odd_palindrome(m: int) -> Tuple[int, int]:
    def palindrome_check(x: int) -> bool:
        s = str(x)
        return s == s[::-1]

    def loop_counter(z: int, alpha_acc: int, beta_acc: int) -> Tuple[int, int]:
        if z > m:
            return alpha_acc, beta_acc
        even_pal = (z % 2 == 0) and palindrome_check(z)
        odd_pal = (z % 2 == 1) and palindrome_check(z)
        if even_pal and not odd_pal:
            return loop_counter(z + 1, alpha_acc + 1, beta_acc)
        elif not even_pal and odd_pal:
            return loop_counter(z + 1, alpha_acc, beta_acc + 1)
        else:
            return loop_counter(z + 1, alpha_acc, beta_acc)

    return loop_counter(1, 0, 0)