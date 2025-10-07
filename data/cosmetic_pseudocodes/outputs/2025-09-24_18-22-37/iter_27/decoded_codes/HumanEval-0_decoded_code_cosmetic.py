from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    pos_alpha: int = 0
    length: int = len(list_of_numbers)
    while pos_alpha < length:
        val_phi: float = list_of_numbers[pos_alpha]
        pos_beta: int = 0
        while pos_beta < length:
            val_omega: float = list_of_numbers[pos_beta]
            if pos_beta != pos_alpha:
                diff_temp: float = val_phi - val_omega
                if diff_temp < 0:
                    diff_temp = -diff_temp
                if not (diff_temp >= threshold_value):
                    return True
            pos_beta += 1
        pos_alpha += 1
    return False