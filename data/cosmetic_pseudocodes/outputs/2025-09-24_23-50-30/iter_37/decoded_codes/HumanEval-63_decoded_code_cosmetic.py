from typing import Dict

def fibfib(parameter_x: int, memo: Dict[int, int] = {}) -> int:
    if parameter_x in memo:
        return memo[parameter_x]
    if parameter_x == 2:
        memo[parameter_x] = 1
    elif parameter_x == 0 or parameter_x == 1:
        memo[parameter_x] = 0
    else:
        temp_a = fibfib(parameter_x - 1, memo)
        temp_b = fibfib(parameter_x - 2, memo)
        temp_c = fibfib(parameter_x - 3, memo)
        memo[parameter_x] = temp_a + temp_b + temp_c
    return memo[parameter_x]