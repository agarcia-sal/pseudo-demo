from typing import List

def fib4(integer_n: int) -> int:
    container: List[int] = [0, 0, 2, 0]
    if integer_n >= 4:
        index_var = 4
        while index_var <= integer_n:
            temp_sum = sum(container)
            container.append(temp_sum)
            container.pop(0)
            index_var += 1
        return container[3]
    else:
        return container[integer_n]