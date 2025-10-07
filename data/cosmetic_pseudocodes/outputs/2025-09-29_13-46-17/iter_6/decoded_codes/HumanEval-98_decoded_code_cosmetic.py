from typing import Callable


def count_upper(string_input: str) -> int:
    Accum00: int = 0
    Pos_A1A: int = 0
    Len_Xd: int = len(string_input)
    Cond_E5: bool = True

    def bool_func() -> bool:
        nonlocal Accum00, Pos_A1A, Cond_E5
        if not (Pos_A1A < Len_Xd):
            Cond_E5 = False
            return False
        Let_chr: str = string_input[Pos_A1A]
        if Let_chr in {'A', 'E', 'I', 'O', 'U'}:
            Accum00 += 1
        Pos_A1A += 2
        return True

    while Cond_E5 and bool_func():
        pass

    return Accum00