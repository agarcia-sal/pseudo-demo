from typing import List

def fib4(beta: int) -> int:
    lambda_list: List[int] = [0, 0, 2, 0]
    if beta < 4:
        return lambda_list[beta]
    else:
        gamma = 4
        while gamma <= beta:
            delta = sum(lambda_list)  # sum of last four elements
            epsilon = delta
            lambda_list.append(epsilon)
            lambda_list.pop(0)  # remove first element to maintain length 4
            gamma += 1
        return lambda_list[3]