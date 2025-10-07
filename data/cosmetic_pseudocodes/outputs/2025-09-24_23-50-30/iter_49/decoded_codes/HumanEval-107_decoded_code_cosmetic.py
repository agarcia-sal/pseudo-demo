from typing import Tuple, List


def even_odd_palindrome(alpha: int) -> Tuple[int, int]:
    def is_palindrome(beta: int) -> bool:
        def reverse_string(chars: List[str], left_index: int, right_index: int) -> List[str]:
            if left_index >= right_index:
                return chars
            chars[left_index], chars[right_index] = chars[right_index], chars[left_index]
            return reverse_string(chars, left_index + 1, right_index - 1)

        char_array = list(str(beta))
        reversed_chars = reverse_string(char_array, 0, len(char_array) - 1)
        return str(beta) == "".join(reversed_chars)

    def loop_counter(gamma: int, delta_even: int, delta_odd: int) -> Tuple[int, int]:
        if gamma > alpha:
            return delta_even, delta_odd
        is_sym = is_palindrome(gamma)
        is_odd = (gamma & 1) == 1
        new_even = delta_even
        new_odd = delta_odd

        if is_sym:
            if is_odd:
                new_odd += 1
            else:
                new_even += 1

        return loop_counter(gamma + 1, new_even, new_odd)

    return loop_counter(1, 0, 0)