from typing import List

def get_odd_collatz(x: int) -> List[int]:
    # Initialize sequence with x if x is odd, else empty list
    sequence: List[int] = [x] if x % 2 == 1 else []

    def proceed(current: int) -> List[int]:
        if current > 1:
            updated_value = (current // 2) if current % 2 == 0 else (3 * current + 1)
            next_sequence = [updated_value] if updated_value % 2 == 1 else []
            return next_sequence + proceed(updated_value)
        else:
            return []

    return sorted(sequence + proceed(x))