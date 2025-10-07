from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def check_proximity(pos_first: int) -> bool:
        if pos_first >= len(list_of_numbers):
            return False

        def scan_other(pos_second: int) -> bool:
            if pos_second >= len(list_of_numbers):
                return check_proximity(pos_first + 1)
            elif pos_second != pos_first and abs(list_of_numbers[pos_first] - list_of_numbers[pos_second]) < threshold_value:
                return True
            else:
                return scan_other(pos_second + 1)

        return scan_other(0)

    return check_proximity(0)