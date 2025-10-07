from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    lambda_var = 0
    length = len(list_of_numbers)
    while lambda_var < length:
        sigma_var = 0
        while sigma_var < length:
            if lambda_var != sigma_var:
                delta_var = list_of_numbers[lambda_var] - list_of_numbers[sigma_var]
                if delta_var < 0:
                    delta_var = -delta_var
                if delta_var < threshold_value:
                    return True
            sigma_var += 1
        lambda_var += 1
    return False