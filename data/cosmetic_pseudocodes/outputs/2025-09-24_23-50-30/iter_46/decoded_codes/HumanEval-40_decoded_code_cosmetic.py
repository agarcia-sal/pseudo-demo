from typing import List

def triples_sum_to_zero(parameter_a: List[int]) -> bool:
    def helper_function(parameter_b: int, parameter_c: int) -> bool:
        if parameter_b < len(parameter_a) - 1:
            if parameter_c < len(parameter_a) - 1:
                if (parameter_a[parameter_b] + parameter_a[parameter_c] + parameter_a[parameter_c + 1]) == 0:
                    return True
                else:
                    return helper_function(parameter_b, parameter_c + 1)
            else:
                return helper_function(parameter_b + 1, parameter_b + 2)
        else:
            return False

    return helper_function(0, 1)