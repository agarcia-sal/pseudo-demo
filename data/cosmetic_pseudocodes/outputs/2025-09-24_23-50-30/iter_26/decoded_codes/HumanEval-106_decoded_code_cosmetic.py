from typing import List

def f(integer_n: int) -> List[int]:
    def compute_factorial(integer_x: int) -> int:
        return 1 if integer_x == 1 else integer_x * compute_factorial(integer_x - 1)

    def compute_sum(integer_x: int) -> int:
        return integer_x * (integer_x + 1) // 2

    def iterate(index_k: int, acc_list: List[int]) -> List[int]:
        if index_k > integer_n:
            return acc_list
        current_res = compute_factorial(index_k) if index_k % 2 == 0 else compute_sum(index_k)
        return iterate(index_k + 1, acc_list + [current_res])

    return iterate(1, [])