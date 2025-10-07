from typing import List

def fib4(parameter_p: int) -> int:
    container_c: List[int] = [0, 0, 2, 0]
    if parameter_p < 4:
        return container_c[parameter_p]
    else:
        index_i: int = 4
        while not (index_i > parameter_p):
            temp_t: int = sum(container_c)
            container_c.append(temp_t)
            container_c.pop(0)
            index_i += 1
        return container_c[3]