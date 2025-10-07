from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        string_form = str(number)
        reversed_string = ''
        idx = len(string_form)
        while idx > 0:
            reversed_string += string_form[idx - 1]
            idx -= 1
        return reversed_string == string_form

    tally_even_palindromes = 0
    tally_odd_palindromes = 0
    count_iterator = 1

    while count_iterator <= n:
        if count_iterator % 2 != 0:
            if is_palindrome(count_iterator):
                tally_odd_palindromes += 1
        else:
            if is_palindrome(count_iterator):
                tally_even_palindromes += 1
        count_iterator += 1

    return (tally_even_palindromes, tally_odd_palindromes)