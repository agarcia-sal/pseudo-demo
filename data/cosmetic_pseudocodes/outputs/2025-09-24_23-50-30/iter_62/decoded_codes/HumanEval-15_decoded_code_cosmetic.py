from typing import List

def string_sequence(integer_p: int) -> str:
    def build_sequence(list_q: List[str], integer_r: int) -> List[str]:
        if integer_r < 0:
            return list_q
        return build_sequence([str(integer_r)] + list_q, integer_r - 1)
    return " ".join(build_sequence([], integer_p))