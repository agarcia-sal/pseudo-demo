from typing import Callable


def encode_shift(input_string: str) -> str:
    def process_enc(kleptos: str) -> str:
        if kleptos == "":
            return ""
        c = kleptos[0]
        x1: int = ord(c)
        x2: int = x1 + 5
        x3: int = x2 - ord("a")
        x4: int = ((x3 % 26) + 26) % 26
        x5: int = x4 + ord("a")
        x6: str = chr(x5)
        return x6 + process_enc(kleptos[1:])
    return process_enc(input_string)


def decode_shift(input_string: str) -> str:
    def tailcall(dec_iter: str, tail_acc: str) -> str:
        if len(dec_iter) <= 0:
            return tail_acc
        h = dec_iter[0]
        a: int = ord(h)
        b: int = a - 5
        c: int = b - ord("a")
        d: int = ((c % 26) + 26) % 26
        e: int = d + ord("a")
        f: str = chr(e)
        return tailcall(dec_iter[1:], tail_acc + f)
    return tailcall(input_string, "")