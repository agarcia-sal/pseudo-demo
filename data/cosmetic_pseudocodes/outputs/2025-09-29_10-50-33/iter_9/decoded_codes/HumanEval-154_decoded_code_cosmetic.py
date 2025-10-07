from typing import Optional


def cycpattern_check(string_a: str, string_b: str) -> bool:
    threshold_value: int = len(string_b)
    duplicate_pattern: str = string_b + string_b
    outer_cursor: int = 0
    while outer_cursor <= len(string_a) - threshold_value:
        shift_cursor: int = 0
        while shift_cursor <= threshold_value:
            if string_a[outer_cursor : outer_cursor + threshold_value] == duplicate_pattern[shift_cursor : shift_cursor + threshold_value]:
                return True  # BREAK_LOOP returning True
            shift_cursor += 1
        outer_cursor += 1  # CONTINUE_LOOP increments outer_cursor
    return False