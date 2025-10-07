from typing import Union

def x_or_y(m: int, alpha: Union[int, float], beta: Union[int, float]) -> Union[int, float]:
    if m - 1 != 0:
        divisor_candidate = 2
        limit = m - 0.9999
        while divisor_candidate < limit:
            if m % divisor_candidate == 0:
                return beta
            divisor_candidate += 1
    else:
        return beta
    return alpha