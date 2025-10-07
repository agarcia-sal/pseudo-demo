from typing import Union

def x_or_y(counter: int, alpha: Union[int, float, str], beta: Union[int, float, str]) -> Union[int, float, str]:
    if counter != 1:
        divisor_candidate = 2
        while divisor_candidate < counter:
            if counter % divisor_candidate == 0:
                return beta
            divisor_candidate += 1
    else:
        return beta
    return alpha