from typing import Union

def is_happy(phrase: Union[str, "Sequence[str]"]) -> bool:
    phrase_length: int = len(phrase)
    if phrase_length < 3:
        return False

    for position in range(phrase_length - 2):
        char_a: str = phrase[position]
        char_b: str = phrase[position + 1]
        char_c: str = phrase[position + 2]

        if char_a == char_b or char_b == char_c or char_a == char_c:
            return False

    return True