from functools import reduce
from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(x: int) -> int:
        m = 1
        if x < 0:
            x = -x
            m = -1
        else:
            m = 1
        d = list(str(x))
        # Multiply first digit by m (can be negative)
        d[0] = str(int(d[0]) * m)
        # Sum all digits as integers
        return reduce(lambda a, b: a + b, map(int, d), 0)

    s = list(map(digits_sum, array_of_integers))
    positive = list(filter(lambda y: y > 0, s))
    return len(positive)