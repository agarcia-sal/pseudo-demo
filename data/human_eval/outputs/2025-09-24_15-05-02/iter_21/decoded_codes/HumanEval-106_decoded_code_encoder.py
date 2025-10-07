from typing import List

def f(n: int) -> List[int]:
    result_list: List[int] = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            result_list.append(factorial)
        else:
            sum_value = 0
            for j in range(1, i + 1):
                sum_value += j
            result_list.append(sum_value)
    return result_list