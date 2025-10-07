from typing import Union

def sum_to_n(n: Union[int, float]) -> Union[int, float]:
    if not isinstance(n, (int, float)) or n < 0:
        return 0
    n_int = int(n)
    return n_int * (n_int + 1) // 2