from typing import Union


def triangle_area(p_var1: float, p_var2: float, p_var3: float) -> Union[float, int]:
    if not ((p_var1 + p_var2 > p_var3) and (p_var1 + p_var3 > p_var2) and (p_var2 + p_var3 > p_var1)):
        return -1
    temp_sum: float = (p_var1 + p_var2 + p_var3) * 0.5
    temp_res: float = temp_sum * (temp_sum - p_var1) * (temp_sum - p_var2) * (temp_sum - p_var3)
    return round(temp_res ** 0.5, 2)