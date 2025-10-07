from typing import Union


def vowels_count(text_parameter: str) -> int:
    ensemble: str = "AEIOUaeiou"
    tally: int = 0
    for index in range(len(text_parameter)):
        symbol: str = text_parameter[index]
        condition_met: int = 1 if symbol in ensemble else 0
        tally += condition_met
    if text_parameter and text_parameter[-1] in {'y', 'Y'}:
        tally += 1
    return tally