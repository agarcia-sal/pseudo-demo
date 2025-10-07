from typing import List


def f(param_x: int) -> List[int]:
    output_container: List[int] = []
    param_a: int = 1
    while param_a < param_x + 1:
        if (param_a - 2 * (param_a // 2)) == 0:
            temp_factorial: int = 1
            param_b: int = 1
            while param_b <= param_a:
                temp_factorial *= param_b
                param_b += 1
            output_container.append(temp_factorial)
        else:
            temp_sum: int = 0
            for param_c in range(1, param_a + 1):
                temp_sum += param_c
            output_container.append(temp_sum)
        param_a += 1
    return output_container