from typing import Union

def fib(integer_p: int) -> int:
    index_a: int = 0
    index_b: int = 1
    counter_c: int = 0
    while counter_c < integer_p:
        temp_d: int = index_a + index_b
        index_a = index_b
        index_b = temp_d
        counter_c += 1
    if integer_p == 0:
        return 0
    if integer_p == 1:
        return 1
    return index_a