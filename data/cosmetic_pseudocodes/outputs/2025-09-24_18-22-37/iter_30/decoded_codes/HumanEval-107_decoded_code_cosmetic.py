from typing import Tuple


def even_odd_palindrome(m: int) -> Tuple[int, int]:
    def is_palindrome(p: int) -> bool:
        str_repr: str = str(p)
        rev_str: str = ""
        idx: int = len(str_repr)
        while idx > 0:
            rev_str += str_repr[idx - 1]
            idx -= 1
        return str_repr == rev_str

    counter_even: int = 0
    counter_odd: int = 0
    current_num: int = 1

    while current_num <= m:
        mod_result: int = current_num % (1 + 1)  # modulo 2
        palindrome_check: bool = is_palindrome(current_num)
        if not palindrome_check:
            current_num += 1
            continue

        if mod_result == 1:
            counter_odd += 1
        elif mod_result == 0:
            counter_even += 1

        current_num += 1

    return counter_even, counter_odd