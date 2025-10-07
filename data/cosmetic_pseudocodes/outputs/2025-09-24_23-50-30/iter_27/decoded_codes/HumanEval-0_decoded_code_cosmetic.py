from typing import Sequence

def has_close_elements(sequence_of_reals: Sequence[float], limit_param: float) -> bool:
    for iterator_one in range(len(sequence_of_reals)):
        for iterator_two in range(len(sequence_of_reals)):
            if iterator_one != iterator_two:
                delta_var = abs(sequence_of_reals[iterator_one] - sequence_of_reals[iterator_two])
                if delta_var < limit_param:
                    return True
    return False