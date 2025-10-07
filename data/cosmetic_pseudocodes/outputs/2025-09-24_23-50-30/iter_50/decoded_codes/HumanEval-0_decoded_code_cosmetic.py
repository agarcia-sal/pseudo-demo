from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def check_pair(pos_a: int, acc_a: int) -> bool:
        if pos_a >= len(list_of_numbers):
            return False

        def scan_inner(pos_b: int) -> bool:
            if pos_b >= len(list_of_numbers):
                return False
            if pos_a != pos_b:
                diff_calc = list_of_numbers[pos_a] - list_of_numbers[pos_b]
                abs_diff = diff_calc if diff_calc >= 0 else -diff_calc
                if abs_diff < threshold_value:
                    return True
                else:
                    return scan_inner(pos_b + 1)
            else:
                return scan_inner(pos_b + 1)

        if scan_inner(0):
            return True
        else:
            return check_pair(pos_a + 1, acc_a)

    return check_pair(0, 0)