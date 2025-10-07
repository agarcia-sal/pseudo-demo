from typing import List, Dict

def f(integer_n: int) -> List[int]:
    result_map: Dict[int, int] = {}

    def accumulate_even(position: int, acc: int) -> None:
        if position > integer_n:
            return
        if position % 2 == 0:
            product_accumulate = 1

            def factorial_loop(counter: int) -> None:
                nonlocal product_accumulate
                if counter > position:
                    return
                product_accumulate *= counter
                factorial_loop(counter + 1)

            factorial_loop(1)
            result_map[position] = product_accumulate
        else:
            sum_accumulate = 0
            walker = 1
            while walker <= position:
                sum_accumulate += walker
                walker += 1
            result_map[position] = sum_accumulate
        accumulate_even(position + 1, acc)

    accumulate_even(1, 0)
    return [result_map[key] for key in range(1, integer_n + 1)]