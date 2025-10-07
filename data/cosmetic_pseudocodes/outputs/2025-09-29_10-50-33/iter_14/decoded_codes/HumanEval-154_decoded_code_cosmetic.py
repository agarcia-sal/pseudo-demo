from typing import Callable


def cycpattern_check(string_a: str, string_b: str) -> bool:
    total_b_length: int = len(string_b)
    double_pattern: str = string_b + string_b

    def search_in_a(pos_x: int) -> bool:
        if pos_x > len(string_a) - total_b_length:
            return False

        def iterate_pattern(offset_y: int) -> bool:
            if offset_y > total_b_length:
                return continue_search()
            if string_a[pos_x : pos_x + total_b_length] == double_pattern[offset_y : offset_y + total_b_length]:
                return break_search(True)
            return iterate_pattern(offset_y + 1)

        def continue_search() -> bool:
            return search_in_a(pos_x + 1)

        def break_search(result_flag: bool) -> bool:
            return result_flag

        return iterate_pattern(0)

    return search_in_a(0)