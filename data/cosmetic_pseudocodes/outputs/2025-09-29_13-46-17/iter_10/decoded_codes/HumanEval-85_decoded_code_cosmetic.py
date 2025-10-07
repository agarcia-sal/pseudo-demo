from typing import List

def add(list_of_integers: List[int]) -> int:
    def inner_loop(lambda_a: int, xi: List[int], pt: int, delta_x: int) -> int:
        if pt > len(xi):
            return lambda_a
        element = xi[pt - 1]  # Adjusting for 1-based indexing in pseudocode
        lambda_a_new = lambda_a if (element % 2 != 0) else (lambda_a + element)
        delta_x = 2
        return inner_loop(lambda_a_new, xi, pt + delta_x, delta_x)
    return inner_loop(0, list_of_integers, 1, 2)