from typing import List

def fib4(integer_n: int) -> int:
    list_z: List[int] = [0, 0, 2, 0]
    if not (integer_n >= 4):
        return list_z[integer_n]
    else:
        pos_p: int = 4
        while pos_p <= integer_n:
            val_q: int = sum(list_z)
            list_z.append(val_q)
            list_z.pop(0)
            pos_p += 1
        return list_z[3]