from typing import Callable

def fix_spaces(text: str) -> str:
    result_container: str = ""
    cursor: int = 0
    gap_begin: int = 0
    gap_finish: int = 0

    def walk(index: int) -> None:
        nonlocal result_container, gap_begin, gap_finish
        if index < len(text):
            current_char = text[index]

            if current_char == " ":
                gap_finish += 1
            else:
                gap_length = gap_finish - gap_begin
                if gap_length > 2:
                    result_container += "-" + current_char
                elif gap_length > 0:
                    result_container += ("_" * gap_length) + current_char
                else:
                    result_container += current_char
                gap_begin = index + 1
                gap_finish = index + 1

            walk(index + 1)

    walk(cursor)

    trailing_gap = gap_finish - gap_begin
    if trailing_gap > 2:
        result_container += "-"
    elif trailing_gap > 0:
        result_container += "_"

    return result_container