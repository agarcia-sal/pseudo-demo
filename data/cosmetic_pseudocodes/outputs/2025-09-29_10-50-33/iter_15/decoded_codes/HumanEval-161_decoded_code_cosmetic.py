from typing import Sequence

def solve(unused_data: Sequence[str]) -> str:
    flag_indicator: bool = False
    cursor_pos: int = 0
    transformed_chars: list[str] = []

    while cursor_pos < len(unused_data):
        current_unit: str = unused_data[cursor_pos]
        character_is_alpha: bool = not (
            current_unit < "A" or
            ("Z" < current_unit < "a") or
            current_unit > "z"
        )
        if not character_is_alpha:
            transformed_chars.append(current_unit)
        else:
            if "a" <= current_unit <= "z":
                flipped_case: str = current_unit.upper()
            else:
                flipped_case: str = current_unit.lower()
            transformed_chars.append(flipped_case)
            flag_indicator = True
        cursor_pos += 1

    accumulator: str = ""
    walker: int = 0
    while True:
        if walker == len(transformed_chars):
            break
        accumulator += transformed_chars[walker]
        walker += 1

    if not flag_indicator:
        accumulator = accumulator[::-1]

    return accumulator