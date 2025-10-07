from typing import Callable


def digits(n: int) -> int:
    accumulation: int = 1
    tally_of_odds: int = 0

    def process_digit(seq: str, idx: int) -> None:
        nonlocal accumulation, tally_of_odds
        if idx == len(seq):
            return
        current_char: str = seq[idx]
        digit_value: int = int(current_char)

        if digit_value % 2 != 0:
            accumulation *= digit_value
            tally_of_odds += 1

        process_digit(seq, idx + 1)

    process_digit(str(n), 0)

    if tally_of_odds != 0:
        return accumulation

    return 0