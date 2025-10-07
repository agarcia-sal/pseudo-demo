from typing import Callable, List, Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    class Result:
        def __init__(self, even: int, odd: int) -> None:
            self.even = even
            self.odd = odd

    def is_palindrome(number: int) -> bool:
        def to_chars(x: int) -> List[int]:
            if x < 10:
                return [x]
            return to_chars(x // 10) + [x % 10]

        def reverse_list(lst: List[int]) -> List[int]:
            if not lst:
                return []
            return reverse_list(lst[1:]) + [lst[0]]

        def eq_lists(a: List[int], b: List[int]) -> bool:
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a[0] != b[0]:
                return False
            return eq_lists(a[1:], b[1:])

        chars = to_chars(number)
        reversed_chars = reverse_list(chars)
        return eq_lists(chars, reversed_chars)

    def count_palindromes(
        index: int,
        even_acc: int,
        odd_acc: int,
        cont: Callable[[Result], Tuple[int, int]],
    ) -> Tuple[int, int]:
        if index > n:
            return cont(Result(even_acc, odd_acc))

        def mod_is_one(x: int) -> bool:
            return (x % 2) != 0

        def mod_is_zero(x: int) -> bool:
            return (x % 2) == 0

        def update_counts(i: int, e: int, o: int) -> Result:
            if mod_is_one(i):
                return Result(e, o + 1) if is_palindrome(i) else Result(e, o)
            else:
                return Result(e + 1, o) if is_palindrome(i) else Result(e, o)

        def continue_with_new_counts(new_res: Result) -> Tuple[int, int]:
            return count_palindromes(index + 1, new_res.even, new_res.odd, cont)

        return continue_with_new_counts(update_counts(index, even_acc, odd_acc))

    return count_palindromes(1, 0, 0, lambda r: (r.even, r.odd))