from typing import Tuple, List


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        s: str = str(number)
        rev_chars: List[str] = []

        def collect_reverse(i: int) -> None:
            if i < 0:
                return
            rev_chars.append(s[i])
            collect_reverse(i - 1)

        collect_reverse(len(s) - 1)
        return s == "".join(rev_chars)

    even_count: int = 0
    odd_count: int = 0

    def recursive_count(g: int, r: int) -> None:
        nonlocal even_count, odd_count
        if r < g:
            return
        if r % 2 == 0:
            if is_palindrome(r):
                even_count += 1
        else:
            if is_palindrome(r):
                odd_count += 1
        recursive_count(g, r - 1)

    recursive_count(1, n)
    return even_count, odd_count