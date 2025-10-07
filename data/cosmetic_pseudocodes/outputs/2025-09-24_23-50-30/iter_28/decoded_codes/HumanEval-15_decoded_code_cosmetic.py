from typing import List


def string_sequence(integer_alpha: int) -> str:
    def build_list(integer_bravo: int, list_charlie: List[str]) -> List[str]:
        if integer_bravo < 0:
            return list_charlie
        else:
            return build_list(integer_bravo - 1, [str(integer_bravo)] + list_charlie)

    return " ".join(build_list(integer_alpha, []))