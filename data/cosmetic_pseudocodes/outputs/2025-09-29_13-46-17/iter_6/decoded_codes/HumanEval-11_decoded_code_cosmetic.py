from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def TMP_char_AZ9M(character_i: str, character_j: str) -> str:
        # Return '1' if characters differ, else '0'
        return '1' if character_i != character_j else '0'

    def recurse_zip(index: int, mem_result: str) -> str:
        if index >= len(string_a):
            return mem_result
        valI = string_a[index]
        valJ = string_b[index]
        next_val = TMP_char_AZ9M(valI, valJ)
        prepend = mem_result + next_val
        return recurse_zip(index + 1, prepend)

    return recurse_zip(0, "")