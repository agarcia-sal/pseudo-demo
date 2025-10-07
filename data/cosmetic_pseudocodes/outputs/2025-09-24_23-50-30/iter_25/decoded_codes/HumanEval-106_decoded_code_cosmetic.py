from typing import List

def f(integer_n: int) -> List[int]:
    output_container: List[int] = []
    counter_p: int = 1
    while counter_p <= integer_n:
        if not (counter_p % 2 != 0):
            accumulator_x: int = 1
            iterator_y: int = 1
            while iterator_y <= counter_p:
                accumulator_x *= iterator_y
                iterator_y += 1
            output_container.append(accumulator_x)
        else:
            accumulator_x = 0
            iterator_y = 1
            while iterator_y <= counter_p:
                accumulator_x += iterator_y
                iterator_y += 1
            output_container.append(accumulator_x)
        counter_p += 1
    return output_container