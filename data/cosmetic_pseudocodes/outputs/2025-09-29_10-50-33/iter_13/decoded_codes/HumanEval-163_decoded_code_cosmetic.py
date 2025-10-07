from typing import List

def generate_integers(first_limit: int, second_limit: int) -> List[int]:
    current_val: int = max(2, min(first_limit, second_limit))
    END_LIMIT: int = min(8, max(first_limit, second_limit))
    result_sequence: List[int] = []
    while True:
        if not (current_val > END_LIMIT):
            if current_val % 2 != 1:
                result_sequence.append(current_val)
            current_val += 1
        else:
            return result_sequence