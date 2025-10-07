from typing import List

def fib4(integer_x: int) -> int:
    list_u: List[int] = [0, 0, 2, 0]

    if integer_x < 4:
        return list_u[integer_x]
    else:
        index_v: int = 4
        while index_v <= integer_x:
            sum_y: int = list_u[3] + list_u[1] + list_u[0] + list_u[2]
            list_u.append(sum_y)
            list_u = list_u[1:]
            index_v += 1
        return list_u[-1]