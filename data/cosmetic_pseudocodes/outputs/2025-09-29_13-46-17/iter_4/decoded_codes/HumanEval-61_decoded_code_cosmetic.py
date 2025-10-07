from typing import Callable


def correct_bracketing(string_of_brackets: str) -> bool:
    def evaluate_position(position_index: int, current_tally: int) -> bool:
        if position_index >= len(string_of_brackets):
            return current_tally == 0

        current_bracket = string_of_brackets[position_index]
        adjusted_tally = current_tally + 1 if current_bracket == "(" else current_tally - 1

        if adjusted_tally < 0:
            return False
        return evaluate_position(position_index + 1, adjusted_tally)

    return evaluate_position(0, 0)