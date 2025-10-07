from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        def str_eq_rev(x: int) -> bool:
            s1 = str(x)
            s2 = s1[::-1]
            return s1 == s2
        return str_eq_rev(number)

    def count_palindromes(i: int, max_limit: int, evens_acc: int, odds_acc: int) -> Tuple[int, int]:
        if i > max_limit:
            return evens_acc, odds_acc
        mod_is_one = (i % 2) != 0
        pal = is_palindrome(i)
        if mod_is_one and pal:
            return count_palindromes(i + 1, max_limit, evens_acc, odds_acc + 1)
        elif (not mod_is_one) and pal:
            return count_palindromes(i + 1, max_limit, evens_acc + 1, odds_acc)
        else:
            return count_palindromes(i + 1, max_limit, evens_acc, odds_acc)

    return count_palindromes(1, n, 0, 0)