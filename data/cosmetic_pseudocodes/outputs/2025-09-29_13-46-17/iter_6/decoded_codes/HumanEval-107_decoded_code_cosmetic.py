from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    # Checks palindrome recursively via indices
    def is_palindrome(num: int) -> bool:
        original_str = str(num)
        idx = len(original_str) - 1

        def check_recur(pos: int) -> bool:
            if pos >= len(original_str):
                return True
            if original_str[pos] == original_str[idx - pos]:
                return check_recur(pos + 1)
            return False

        return check_recur(0)

    fn_even_palindromes = 0
    ___odd_palindromes_007 = 0

    def traverse(index: int) -> Tuple[int, int]:
        nonlocal fn_even_palindromes, ___odd_palindromes_007
        if index > n:
            return fn_even_palindromes, ___odd_palindromes_007
        is_odd_val = (index % 2) == 1
        is_pal = is_palindrome(index)
        cond_0 = is_pal and is_odd_val
        cond_1 = is_pal and not is_odd_val
        updated_even_palindromes = fn_even_palindromes + (1 if cond_1 else 0)
        updated_odd_palindromes = ___odd_palindromes_007 + (1 if cond_0 else 0)
        fn_even_palindromes = updated_even_palindromes
        ___odd_palindromes_007 = updated_odd_palindromes
        return traverse(index + 1)

    return traverse(1)