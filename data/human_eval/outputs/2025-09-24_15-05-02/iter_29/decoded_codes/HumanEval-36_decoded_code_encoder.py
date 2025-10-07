from typing import List

def fizz_buzz(integer_n: int) -> int:
    list_ns: List[int] = []
    for integer_i in range(integer_n):
        if integer_i % 11 == 0 or integer_i % 13 == 0:
            list_ns.append(integer_i)
    string_s: str = ''.join(str(num) for num in list_ns)
    integer_ans: int = 0
    for character_c in string_s:
        integer_ans += (character_c == '7')
    return integer_ans