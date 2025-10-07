from typing import List

def f(integer_n: int) -> List[int]:
    array_result: List[int] = [0] * integer_n
    var_x: int = 1
    while var_x <= integer_n:
        if var_x % 2 == 0:
            var_y: int = 1
            var_z: int = 1
            while True:
                if var_z > var_x:
                    array_result[var_x - 1] = var_y
                    break
                var_y *= var_z
                var_z += 1
        else:
            var_a: int = 0
            var_b: int = 1
            while True:
                if var_b > var_x:
                    array_result[var_x - 1] = var_a
                    break
                var_a += var_b
                var_b += 1
        var_x += 1
    return array_result