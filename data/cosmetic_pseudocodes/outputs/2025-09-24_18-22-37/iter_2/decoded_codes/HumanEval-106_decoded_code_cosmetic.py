from typing import List


def f(integer_n: int) -> List[int]:
    output: List[int] = []
    counter_x: int = 1
    while counter_x <= integer_n:
        if (counter_x % 2) == 0:
            prod: int = 1
            multiply_idx: int = 1
            while multiply_idx <= counter_x:
                prod *= multiply_idx
                multiply_idx += 1
            output.append(prod)
        else:
            sum_acc: int = 0
            add_idx: int = 1
            while add_idx <= counter_x:
                sum_acc += add_idx
                add_idx += 1
            output.append(sum_acc)
        counter_x += 1
    return output