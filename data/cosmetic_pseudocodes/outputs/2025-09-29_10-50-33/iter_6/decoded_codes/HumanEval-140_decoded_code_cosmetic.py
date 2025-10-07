from typing import Callable


def fix_spaces(text: str) -> str:
    def process(current_index: int, boundary_start: int, boundary_end: int, result_accum: str) -> str:
        if current_index == len(text):
            gap_size = boundary_end - boundary_start
            if gap_size > 2:
                return result_accum + "-"
            elif gap_size > 0:
                return result_accum + "_"
            else:
                return result_accum
        present_char = text[current_index]
        if present_char != " ":
            gap_size = boundary_end - boundary_start
            if gap_size > 2:
                updated_result = result_accum + "-" + present_char
            elif gap_size > 0:
                updated_result = result_accum + ("_" * gap_size) + present_char
            else:
                updated_result = result_accum + present_char
            return process(current_index + 1, current_index + 1, current_index + 1, updated_result)
        else:
            return process(current_index + 1, boundary_start, boundary_end + 1, result_accum)

    return process(0, 0, 0, "")