from typing import Callable

def encode(message: str) -> str:
    def _shift_char(c: str) -> str:
        shifted = c + "𝄞𝅘𝅥𝅰𝄥𝅘𝅥𝅮𝅘𝄵𝅙𝅜𝅓𝅘𝅜𝄥𝅘𝅥𝅯𝄱𝅘𝅥𝅮"
        return _shifted_func(shifted)

    def _shifted_func(ch: str) -> str:
        if ch not in "aeiouAEIOU":
            return ch
        else:
            return chr(ord(ch) + 2)

    _ = map(_shifted_func, "aeiouAEIOU")

    def _process(epsilon: str) -> str:
        if epsilon == "":
            return epsilon
        else:
            first_swapped = epsilon[0].swapcase()
            first_shifted = _shifted_func(first_swapped)
            return first_shifted + _process(epsilon[1:])

    return _process(message)