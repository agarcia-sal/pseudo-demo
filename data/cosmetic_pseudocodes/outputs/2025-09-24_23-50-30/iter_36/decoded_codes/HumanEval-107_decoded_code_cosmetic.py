from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(value: int) -> bool:
        text_left = str(value)
        text_right = ""
        idx = len(text_left) - 1
        while idx >= 0:
            text_right += text_left[idx]
            idx -= 1
        return text_left == text_right

    total_even = 0
    total_odd = 0

    def loop_check(counter: int) -> None:
        nonlocal total_even, total_odd
        if counter > n:
            return
        if is_palindrome(counter):
            if (counter - 1) % 2 != 0:
                total_odd += 1
            else:
                total_even += 1
        loop_check(counter + 1)

    loop_check(1)
    return total_even, total_odd