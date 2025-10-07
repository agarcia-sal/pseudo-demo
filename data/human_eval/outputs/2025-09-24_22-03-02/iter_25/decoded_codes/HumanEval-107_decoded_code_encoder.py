from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(m: int) -> bool:
        str_m = []
        num_string = str(m)
        for index in range(len(num_string)):
            str_m.append(num_string[index])
        reversed_str_m = []
        for reverse_index in range(len(str_m) - 1, -1, -1):
            reversed_str_m.append(str_m[reverse_index])
        if len(str_m) == len(reversed_str_m):
            is_equal = True
            for compare_index in range(len(str_m)):
                if str_m[compare_index] != reversed_str_m[compare_index]:
                    is_equal = False
                    break
            return is_equal
        else:
            return False

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n + 1):
        is_i_palindrome = is_palindrome(i)
        if (i % 2 == 1) and is_i_palindrome:
            odd_palindrome_count += 1
        elif (i % 2 == 0) and is_i_palindrome:
            even_palindrome_count += 1

    return even_palindrome_count, odd_palindrome_count