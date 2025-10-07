from typing import List


def f(param_x: int) -> List[int]:
    output_seq: List[int] = []

    def accumulate_factorial(current_k: int, limit_p: int, product_acc: int) -> int:
        if current_k > limit_p:
            return product_acc
        else:
            return accumulate_factorial(current_k + 1, limit_p, product_acc * current_k)

    def accumulate_sum(current_m: int, limit_n: int, total_acc: int) -> int:
        if current_m > limit_n:
            return total_acc
        else:
            return accumulate_sum(current_m + 1, limit_n, total_acc + current_m)

    def process_index(index_v: int) -> None:
        if not (index_v % 2 != 0):
            factorial_result = accumulate_factorial(1, index_v, 1)
            output_seq.append(factorial_result)
        else:
            summation_result = accumulate_sum(1, index_v, 0)
            output_seq.append(summation_result)

    def iterate_loop(counter_z: int) -> None:
        if counter_z > param_x:
            return
        process_index(counter_z)
        iterate_loop(counter_z + 1)

    iterate_loop(1)

    return output_seq