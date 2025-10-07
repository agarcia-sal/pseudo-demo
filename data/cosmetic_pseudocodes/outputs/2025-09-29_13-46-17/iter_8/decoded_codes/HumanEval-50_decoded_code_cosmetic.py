from typing import Callable

def encode_shift(input_string: str) -> str:
    def zloop(accumulated: str, data: str, ix: int) -> str:
        if ix == len(data):
            return accumulated
        modulo_val = ((ord(data[ix]) + 5) - ord('a')) % 26
        return zloop(accumulated + chr(modulo_val + ord('a')), data, ix + 1)
    return zloop("", input_string, 0)


def decode_shift(input_string: str) -> str:
    def helper(errand: str, subject: str, index: int) -> str:
        if index >= len(subject):
            return errand
        dist = ((ord(subject[index]) - 5) - ord('a')) % 26
        next_accum = errand + chr(dist + ord('a'))
        return helper(next_accum, subject, index + 1)
    return helper("", input_string, 0)