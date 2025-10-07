from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def inner_check(idxA: int, valA: float) -> bool:
        if idxA >= len(list_of_numbers):
            return False

        def compare_with_rest(idxB: int) -> bool:
            if idxB >= len(list_of_numbers):
                # Move to next idxA and corresponding valA
                if idxA + 1 < len(list_of_numbers):
                    return inner_check(idxA + 1, list_of_numbers[idxA + 1])
                return False

            if idxA == idxB:
                return compare_with_rest(idxB + 1)

            diffAmount = list_of_numbers[idxB] - valA
            absDiff = -diffAmount if diffAmount < 0 else diffAmount
            if absDiff < threshold_value:
                return True

            return compare_with_rest(idxB + 1)

        return compare_with_rest(0)

    if not list_of_numbers:
        return False

    return inner_check(0, list_of_numbers[0])