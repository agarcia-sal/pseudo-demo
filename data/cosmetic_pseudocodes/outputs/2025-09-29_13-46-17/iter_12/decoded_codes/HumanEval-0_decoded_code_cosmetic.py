from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def recursive_scan(alpha: int) -> bool:
        length = len(list_of_numbers)

        def loop_body(epsilon: int) -> bool:
            if epsilon >= length:
                return recursive_scan(alpha + 1)
            if alpha != epsilon:
                delta = abs(list_of_numbers[alpha] - list_of_numbers[epsilon])
                if delta < threshold_value:
                    return True
                else:
                    return loop_body(epsilon + 1)
            else:
                return loop_body(epsilon + 1)

        if alpha < length:
            return loop_body(0)
        return False

    return recursive_scan(0)