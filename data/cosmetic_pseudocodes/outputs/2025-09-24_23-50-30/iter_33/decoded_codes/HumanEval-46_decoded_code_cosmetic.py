from typing import List

def fib4(integer_q: int) -> int:
    list_x: List[int] = [0, 0, 2, 0]
    if integer_q < 4:
        return list_x[integer_q]

    counter_z: int = 4
    while counter_z <= integer_q:
        sum_k: int = sum(list_x)
        list_x.append(sum_k)
        list_x.pop(0)
        counter_z += 1

    return list_x[-1]