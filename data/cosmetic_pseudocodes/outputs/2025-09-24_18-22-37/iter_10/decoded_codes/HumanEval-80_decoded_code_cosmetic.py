from typing import Sequence

def is_happy(glyph_set: Sequence[str]) -> bool:
    if len(glyph_set) < 3:
        return False

    for counter in range(len(glyph_set) - 2):
        first_char = glyph_set[counter]
        second_char = glyph_set[counter + 1]
        third_char = glyph_set[counter + 2]

        if first_char == second_char:
            return False
        if second_char == third_char:
            return False
        if third_char == first_char:
            return False

    return True