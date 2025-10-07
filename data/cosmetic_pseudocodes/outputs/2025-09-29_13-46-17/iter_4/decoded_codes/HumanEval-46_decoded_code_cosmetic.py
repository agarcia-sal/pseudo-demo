from typing import List

def fib4(integer_n: int) -> int:
    vector_alpha: List[int] = [0, 0, 2, 0]

    def accumulate(beta_index: int) -> int:
        nonlocal vector_alpha
        if beta_index < 4:
            return vector_alpha[beta_index]
        summation = sum(vector_alpha)
        vector_alpha = [vector_alpha[1], vector_alpha[2], vector_alpha[3], summation]
        return accumulate(beta_index - 1)

    return accumulate(integer_n)