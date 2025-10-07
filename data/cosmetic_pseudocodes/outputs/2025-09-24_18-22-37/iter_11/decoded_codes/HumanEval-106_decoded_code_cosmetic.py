from typing import List

def f(integer_n: int) -> List[int]:
    list_output: List[int] = []
    counter_outer: int = 1
    while counter_outer <= integer_n:
        temp_modulo: int = counter_outer % 2
        if temp_modulo == 0:
            temp_factorial: int = 1
            counter_inner_factorial: int = 1
            while True:
                if counter_inner_factorial > counter_outer:
                    break
                temp_factorial *= counter_inner_factorial
                counter_inner_factorial += 1
            list_output.append(temp_factorial)
        else:
            temp_sum: int = 0
            counter_inner_sum: int = 1
            while counter_inner_sum <= counter_outer:
                temp_sum += counter_inner_sum
                counter_inner_sum += 1
            list_output.append(temp_sum)
        counter_outer += 1
    return list_output