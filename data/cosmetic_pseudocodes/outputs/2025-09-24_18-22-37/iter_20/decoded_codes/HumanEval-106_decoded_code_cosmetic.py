from typing import List

def f(param_x: int) -> List[int]:
    collection_m: List[int] = []
    counter_y: int = 1
    while counter_y <= param_x:
        remainder_val = counter_y % 2
        if remainder_val == 0:
            acc_factorial = 1
            iterator_z = 1
            while iterator_z <= counter_y:
                acc_factorial *= iterator_z
                iterator_z += 1
            collection_m.append(acc_factorial)
        else:
            acc_sum = 0
            iterator_w = 1
            while iterator_w <= counter_y:
                acc_sum += iterator_w
                iterator_w += 1
            collection_m.append(acc_sum)
        counter_y += 1
    return collection_m