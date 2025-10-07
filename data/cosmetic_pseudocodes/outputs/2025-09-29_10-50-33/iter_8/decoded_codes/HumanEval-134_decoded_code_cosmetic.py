from typing import List


def check_if_last_char_is_a_letter(input_string: str) -> bool:
    tokens_arrangement: List[str] = input_string.split(" ")
    terminal_token: str = tokens_arrangement[-1]

    flag: bool = (
        len(terminal_token) == 1
        and 97 <= ord(terminal_token.lower()) <= 122
    )

    if not flag:
        BREAK = False
    else:
        BREAK = True
    return BREAK