from typing import List

def fib4(integer_n: int) -> int:
    results: List[int] = [0, 0, 2, 0]
    if integer_n >= 4:
        while True:
            current_length = len(results)
            if current_length > integer_n:
                break
            summation = sum(results[current_length - 4 : current_length])
            results.append(summation)
            results = results[1:]
        return results[-1]
    else:
        return results[integer_n]