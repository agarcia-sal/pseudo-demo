from typing import List

def f(integer_n: int) -> List[int]:
    result_list: List[int] = []

    def inner_accumulate_even(current_pos: int, accum_prod: int) -> int:
        if current_pos > integer_n:
            return accum_prod
        if current_pos % 2 != 0:
            return inner_accumulate_even(current_pos + 1, accum_prod)

        def inner_factorial(k: int, accumulator: int) -> int:
            if k > current_pos:
                return accumulator
            return inner_factorial(k + 1, accumulator * k)

        result_list.append(inner_factorial(1, 1))
        return inner_accumulate_even(current_pos + 1, accum_prod)

    def inner_accumulate_odd(index: int, accum_sum: int) -> int:
        if index > integer_n:
            return accum_sum
        if index % 2 == 0:
            return inner_accumulate_odd(index + 1, accum_sum)

        def inner_summation(k: int, acc: int) -> int:
            if k > index:
                return acc
            return inner_summation(k + 1, acc + k)

        result_list.append(inner_summation(1, 0))
        return inner_accumulate_odd(index + 1, accum_sum)

    _ = inner_accumulate_even(1, 1)
    _ = inner_accumulate_odd(1, 0)
    return result_list