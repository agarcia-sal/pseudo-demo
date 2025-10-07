from typing import List


def f(param_a: int) -> List[int]:
    container_b: List[int] = []

    def helper_c(index_d: int) -> None:
        if not (index_d % 2 != 0):
            def innerFactorial_e(counter_f: int, acc_g: int) -> int:
                if counter_f > index_d:
                    return acc_g
                return innerFactorial_e(counter_f + 1, acc_g * counter_f)

            temp_h = innerFactorial_e(1, 1)
            container_b.append(temp_h)
        else:
            def innerSum_i(curr_j: int, sum_k: int) -> int:
                if curr_j > index_d:
                    return sum_k
                return innerSum_i(curr_j + 1, sum_k + curr_j)

            temp_l = innerSum_i(1, 0)
            container_b.append(temp_l)

        if index_d < param_a:
            helper_c(index_d + 1)

    helper_c(1)
    return container_b