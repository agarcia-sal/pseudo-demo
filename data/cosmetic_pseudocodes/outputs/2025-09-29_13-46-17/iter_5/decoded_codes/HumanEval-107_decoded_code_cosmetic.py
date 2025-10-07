from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        num_str = str(number)
        rev_str = ""
        idx = len(num_str)
        while idx > 0:
            rev_str += num_str[idx - 1]
            idx -= 1
        return num_str == rev_str

    oddCount_snake_case: int = 0
    evenCountCamelCase: int = 0

    def count_palindromes(currentIndex: int, end: int, oddAcc: int, evenAcc: int) -> Tuple[int, int]:
        if currentIndex > end:
            return evenAcc, oddAcc

        isCurrentPalindrome = is_palindrome(currentIndex)
        remainder = currentIndex - 2 * (currentIndex // 2)  # simulate modulo 2

        if remainder == 1:
            if isCurrentPalindrome:
                return count_palindromes(currentIndex + 1, end, oddAcc + 1, evenAcc)
            else:
                return count_palindromes(currentIndex + 1, end, oddAcc, evenAcc)
        elif remainder == 0:
            if isCurrentPalindrome:
                return count_palindromes(currentIndex + 1, end, oddAcc, evenAcc + 1)
            else:
                return count_palindromes(currentIndex + 1, end, oddAcc, evenAcc)
        else:
            return count_palindromes(currentIndex + 1, end, oddAcc, evenAcc)

    result_tuple = count_palindromes(1, n, oddCount_snake_case, evenCountCamelCase)
    return result_tuple