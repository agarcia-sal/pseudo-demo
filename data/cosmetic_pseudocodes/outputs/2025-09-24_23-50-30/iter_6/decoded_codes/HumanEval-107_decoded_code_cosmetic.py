from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(num: int) -> bool:
        str_num = str(num)
        reversed_str = ""
        idx = len(str_num) - 1
        while idx >= 0:
            reversed_str += str_num[idx]
            idx -= 1
        return str_num == reversed_str

    count_even = 0
    count_odd = 0
    current_val = 1

    while current_val <= n:
        if not is_palindrome(current_val):
            current_val += 1
            continue

        # equivalent to (current_val - 1 * (current_val // 2) * 2)
        # using integer division to align with the pseudocode's intention
        remainder = current_val - 1 * (current_val // 2) * 2
        if remainder == 1:
            count_odd += 1
        elif remainder == 0:
            count_even += 1

        current_val += 1

    return count_even, count_odd