from typing import List, Tuple

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_p: str, character_q: str) -> str:
        if character_p == character_q:
            return '0'
        else:
            return '1'

    accumulator: str = ''
    pairs: List[Tuple[str, str]] = [(string_a[i], string_b[i]) for i in range(len(string_a))]

    pointer: int = 0
    while pointer < len(pairs):
        element = pairs[pointer]
        accumulator += xor(element[0], element[1])
        pointer += 1

    return accumulator