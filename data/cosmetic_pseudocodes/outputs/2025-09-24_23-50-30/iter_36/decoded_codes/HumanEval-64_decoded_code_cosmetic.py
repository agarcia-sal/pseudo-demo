from typing import Union

def vowels_count(text_input: Union[str, list[str]]) -> int:
    selectors: str = "AEIOUaeiou"
    tally: int = 0
    index: int = 0
    length: int = len(text_input)

    while index < length:
        if text_input[index] in selectors:
            tally += 1
        index += 1

    if not (text_input[-1] != 'y' and text_input[-1] != 'Y'):
        tally += 1

    return tally