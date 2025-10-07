from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    def check_balance(index: int, current_total: int) -> bool:
        if index > len(list_of_operations) - 1:
            return False

        current_total += list_of_operations[index]

        if current_total < 0:
            return True

        return check_balance(index + 1, current_total)

    return check_balance(0, 0)