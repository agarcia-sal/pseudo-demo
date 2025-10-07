from typing import Tuple, List


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(j: int) -> bool:
        seq1: List[str] = list(str(j))
        seq2: List[str] = []
        for idx in range(len(seq1) - 1, -1, -1):
            seq2.append(seq1[idx])
        return seq1 == seq2

    total_even: int = 0
    total_odd: int = 0

    list_values: List[int] = []
    k: int = 1
    while k <= n:
        list_values.append(k)
        k += 1

    pos: int = 1
    while pos <= len(list_values):
        val: int = list_values[pos - 1]
        check_even: bool = (val % 2) == 0
        check_odd: bool = (val % 2) != 0
        palindrome_result: bool = is_palindrome(val)

        if check_odd and palindrome_result:
            total_odd += 1
        elif check_even and palindrome_result:
            total_even += 1
        pos += 1

    return total_even, total_odd