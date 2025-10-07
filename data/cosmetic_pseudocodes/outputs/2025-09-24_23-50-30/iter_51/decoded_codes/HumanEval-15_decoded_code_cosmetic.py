from typing import List

def string_sequence(n_integer: int) -> str:
    def to_string_list(index_current: int, collected_list: List[str]) -> List[str]:
        if index_current > n_integer:
            return collected_list
        else:
            return to_string_list(index_current + 1, collected_list + [str(index_current)])
    return " ".join(to_string_list(0, []))