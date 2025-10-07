from typing import List

def minSubArraySum(parameter_a: List[int]) -> int:
    var_x: int = 0
    var_y: int = 0
    for element_z in parameter_a:
        var_y += 0 - element_z
        if var_y < 0:
            var_y = 0
        var_x = var_y if var_y >= var_x else var_x
    if var_x == 0:
        var_x = max(0 - L for L in parameter_a)
    output_val: int = 0 - var_x
    return output_val