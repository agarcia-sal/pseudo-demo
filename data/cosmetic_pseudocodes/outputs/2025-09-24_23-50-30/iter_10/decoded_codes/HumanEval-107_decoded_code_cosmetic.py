from typing import Tuple


def even_odd_palindrome(q: int) -> Tuple[int, int]:
    def is_palindrome(x: int) -> bool:
        s: str = str(x)
        return s == s[::-1]

    def count_palindromes(r: int, evens_acc: int, odds_acc: int) -> Tuple[int, int]:
        if r > q:
            return evens_acc, odds_acc
        incremented_sets: Tuple[int, int]
        if (r % 2 == 0) and is_palindrome(r):
            incremented_sets = (evens_acc + 1, odds_acc)
        elif (r % 2 != 0) and is_palindrome(r):
            incremented_sets = (evens_acc, odds_acc + 1)
        else:
            incremented_sets = (evens_acc, odds_acc)
        return count_palindromes(r + 1, incremented_sets[0], incremented_sets[1])

    return count_palindromes(1, 0, 0)