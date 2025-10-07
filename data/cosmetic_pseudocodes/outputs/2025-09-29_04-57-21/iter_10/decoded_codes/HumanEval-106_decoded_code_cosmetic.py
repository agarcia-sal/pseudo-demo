from typing import List

def f(integer_n: int) -> List[int]:
    output_array: List[int] = []
    counter = 1

    def factorial_accumulate(current: int, max_val: int) -> int:
        if current > max_val:
            return 1
        else:
            return current * factorial_accumulate(current + 1, max_val)

    while counter <= integer_n:
        if counter % 2 == 0:
            calc_factorial = factorial_accumulate(1, counter)
            output_array.append(calc_factorial)
        else:
            calc_sum = 0
            addend = 1
            while addend <= counter:
                calc_sum += addend
                addend += 1
            output_array.append(calc_sum)
        counter += 1

    return output_array