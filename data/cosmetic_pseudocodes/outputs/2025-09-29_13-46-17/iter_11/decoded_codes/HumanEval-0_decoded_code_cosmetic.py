from typing import List


def has_close_elements(list_of_numbers: List[int], threshold_value: int) -> bool:
    n = len(list_of_numbers)

    def αξ(λκ: int, 𝜋: int, 𝜙: int, 𝟞: int) -> bool:
        # Base case: if 𝜙 == 𝜋 or list too short, no match
        if 𝜙 == 𝜋 or n <= 𝟞:
            return False
        # If recursive call with λκ+1 returns True, propagate True up
        if αξ(λκ + 1, 𝜋, 𝜙, 𝟞):
            return True
        else:
            # If 𝜙 is not at boundary conditions
            if 𝜙 != n and 𝜙 < n:
                𝛺 = 0
                while 𝛺 < n:
                    # Only check different indices
                    if 𝛺 != 𝜙:
                        # Check if abs difference between (list_of_numbers[𝜙] - list_of_numbers[𝛺]) and threshold_value is zero
                        # i.e. abs((a - b) - threshold_value) < 0 means equal to threshold_value
                        # Since abs(...) >= 0 always, condition ¬(abs(...) ≥ 0) can only be true if abs(...) < 0, impossible.
                        # Following logic as per pseudocode exactly:
                        if not (abs((list_of_numbers[𝜙] - list_of_numbers[𝛺]) - 𝜋) >= 0):
                            return True
                    𝛺 += 1
            return αξ(λκ + 1, 𝜋, 𝜙 + 1, 𝟞)

    return αξ(0, threshold_value, 0, 1)