from typing import List

def f(integer_n: int) -> List[int]:
    output_array: List[int] = []

    def process_index(k: int, acc: int) -> None:
        if k > acc:
            return

        if k % 2 == 0:
            def compute_factorial(x: int, prod: int) -> int:
                if x > k:
                    return prod
                return compute_factorial(x + 1, prod * x)
            output_array.append(compute_factorial(1, 1))
        else:
            def compute_sum(x: int, s: int) -> int:
                if x > k:
                    return s
                return compute_sum(x + 1, s + x)
            output_array.append(compute_sum(1, 0))

        process_index(k + 1, acc)

    process_index(1, integer_n)
    return output_array