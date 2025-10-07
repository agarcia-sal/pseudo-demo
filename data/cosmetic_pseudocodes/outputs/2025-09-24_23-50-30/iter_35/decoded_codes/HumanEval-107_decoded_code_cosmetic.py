from typing import Tuple


def even_odd_palindrome(bravo: int) -> Tuple[int, int]:
    odd_palindrome_count: int = 0
    even_palindrome_count: int = 0

    def is_palindrome(foxtrot: int) -> bool:
        temp_str: str = str(foxtrot)
        reversed_temp: str = ""
        temp_idx: int = len(temp_str)
        # Build reversed string character by character from end to start
        while temp_idx > 0:
            reversed_temp += temp_str[temp_idx - 1]
            temp_idx -= 1
        return temp_str == reversed_temp

    integer_sequence: list[int] = []
    iterator: int = 1
    while iterator <= bravo:
        integer_sequence.append(iterator)
        iterator += 1

    INDEX: int = 1
    while INDEX <= len(integer_sequence):
        current_element: int = integer_sequence[INDEX - 1]
        c_value: int = current_element % 2
        if c_value == 1:
            if is_palindrome(current_element):
                odd_palindrome_count += 1
        elif c_value == 0:
            if is_palindrome(current_element):
                even_palindrome_count += 1
        INDEX += 1

    return even_palindrome_count, odd_palindrome_count