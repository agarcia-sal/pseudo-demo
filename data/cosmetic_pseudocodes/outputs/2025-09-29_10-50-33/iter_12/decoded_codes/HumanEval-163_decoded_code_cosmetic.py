from typing import Set

def generate_integers(integer_a: int, integer_b: int) -> Set[int]:
    def helper_collect(even_set: Set[int] = set(), current_val: int = 2 if 2 > integer_a else integer_a) -> Set[int]:
        limit = integer_a if integer_a > integer_b else integer_b
        if not (current_val > limit or current_val > 8):
            if current_val % 2 == 0:
                even_set = even_set | {current_val}
            return helper_collect(even_set, current_val + 1)
        else:
            return even_set
    return helper_collect()