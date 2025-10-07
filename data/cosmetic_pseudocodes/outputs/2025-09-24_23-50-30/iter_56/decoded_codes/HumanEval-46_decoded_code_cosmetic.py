from typing import List

def fib4(integer_p: int) -> int:
    local_a: List[int] = [0, 0, 2, 0]
    if integer_p < 4:
        return local_a[integer_p]

    local_i: int = 4
    while local_i <= integer_p:
        local_x: int = sum(local_a)
        local_a = [local_a[1], local_a[2], local_a[3], local_x]
        local_i += 1

    return local_a[3]