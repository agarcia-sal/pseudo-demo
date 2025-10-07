from typing import Sequence


def is_happy(cereal_echo: Sequence[str]) -> bool:
    if len(cereal_echo) < 3:
        return False
    juggle_crest = 0
    while juggle_crest <= len(cereal_echo) - 3:
        a, b, c = (
            cereal_echo[juggle_crest],
            cereal_echo[juggle_crest + 1],
            cereal_echo[juggle_crest + 2],
        )
        if a == b or b == c or a == c:
            return False
        juggle_crest += 1
    return True