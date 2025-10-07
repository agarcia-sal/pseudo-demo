from typing import List

def string_sequence(integer_n: int) -> str:
    def number_to_string_list(current: int, limit: int, accumulator: List[str]) -> List[str]:
        if current > limit:
            return accumulator
        return number_to_string_list(current + 1, limit, accumulator + [str(current)])

    string_numbers: List[str] = number_to_string_list(0, integer_n, [])
    return " ".join(string_numbers)