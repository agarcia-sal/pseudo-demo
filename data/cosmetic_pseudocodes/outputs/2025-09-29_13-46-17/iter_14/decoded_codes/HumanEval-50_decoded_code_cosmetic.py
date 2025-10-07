from typing import Callable


def encode_shift(input_string: str) -> str:
    result: str = ""
    length: int = len(input_string)
    base_ord: Callable[[str], int] = lambda _: ord("a")
    shift_func: Callable[[int], int] = lambda c: (c + 5 - base_ord("")) % 26 + base_ord("")  # lowercase 'a'=97
    chr_func: Callable[[int], str] = lambda c: chr(c)

    def helper(index: int) -> str:
        nonlocal result
        if index == length:
            return result
        c_ord = ord(input_string[index])
        shifted = shift_func(c_ord)
        shifted_char = chr_func(shifted)
        result += shifted_char
        return helper(index + 1)

    return helper(0)


def decode_shift(input_string: str) -> str:
    result: str = ""
    length: int = len(input_string)
    base_ord: Callable[[str], int] = lambda _: ord("a")
    shift_func: Callable[[int], int] = lambda c: (c - 5 - base_ord("")) % 26 + base_ord("")
    chr_func: Callable[[int], str] = lambda c: chr(c)

    def helper(index: int) -> str:
        nonlocal result
        if index == length:
            return result
        c_ord = ord(input_string[index])
        shifted = shift_func(c_ord)
        shifted_char = chr_func(shifted)
        result += shifted_char
        return helper(index + 1)

    return helper(0)