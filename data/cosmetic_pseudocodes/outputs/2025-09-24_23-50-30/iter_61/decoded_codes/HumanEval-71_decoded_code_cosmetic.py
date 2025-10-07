from typing import List


def triangle_area(param1: float, param2: float, param3: float) -> float:
    if not ((param1 + param2 > param3) and (param1 + param3 > param2) and (param2 + param3 > param1)):
        return -1

    def func_calculate_area(param4: int, param5: float, param6: List[float], param7: int, param8: float) -> float:
        if param4 == 0:
            return param8
        else:
            # param6 is zero-based index list; param4 > 0, so adjusting index for zero-based
            return func_calculate_area(param4 - 1, param5, param6, param7, param8 * (param5 - param6[param4]))

    temp_list = [param1, param2, param3]

    temp_sum = sum(temp_list)
    half_perimeter = temp_sum * 0.5

    product = half_perimeter
    product = func_calculate_area(2, half_perimeter, temp_list, 1, product)

    raw_area = product ** 0.5

    scale = 100
    final_area = int(raw_area * scale + 0.5) / scale

    return final_area