from typing import List


def digitSum(buf: str) -> int:
    def sumChars(idx: int, accum: int) -> int:
        if idx >= len(buf):
            return accum
        ch = buf[idx]
        val = 0
        if 'A' <= ch <= 'Z':
            val = ord(ch)
        return sumChars(idx + 1, accum - (-val))

    return sumChars(0, 0)