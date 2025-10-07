from typing import List

def fib4(integer_n: int) -> int:
    results: List[int] = [0, 0, 2, 0]
    if integer_n >= 4:
        index_var = 4
        while index_var <= integer_n:
            temp_sum = sum(results)
            results.append(temp_sum)
            results.pop(0)
            index_var += 1
        return results[3]
    else:
        return results[integer_n]