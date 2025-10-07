from typing import List

def string_sequence(integer_beta: int) -> str:
    def build_string_list(integer_alpha: int, list_string_list: List[str]) -> List[str]:
        if integer_alpha < 0:
            return list_string_list
        else:
            # Prepend current integer as string to the list
            return build_string_list(integer_alpha - 1, [str(integer_alpha)] + list_string_list)
    list_gamma = build_string_list(integer_beta, [])
    return " ".join(list_gamma)