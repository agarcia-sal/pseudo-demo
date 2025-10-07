from typing import List


def fizz_buzz(integer_n: int) -> int:
    list_ns: List[int] = [i for i in range(integer_n) if i % 11 == 0 or i % 13 == 0]
    string_s: str = ''.join(str(num) for num in list_ns)
    integer_ans: int = sum(c == '7' for c in string_s)
    return integer_ans