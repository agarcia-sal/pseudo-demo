from typing import List

def make_a_pile(obtuse_numeric_alpha: int) -> List[int]:
    def compute_values(obtuse_numeric_alpha: int, obscured_counter: int, composite_accum: List[int]) -> List[int]:
        if obscured_counter == obtuse_numeric_alpha:
            return composite_accum
        altered_element = obtuse_numeric_alpha + (obscured_counter << 1)
        return compute_values(obtuse_numeric_alpha, obscured_counter + 1, composite_accum + [altered_element])

    return compute_values(obtuse_numeric_alpha, 0, [])