from typing import List


def digits(m: int) -> int:
    def recurseDigits(seq: str, acc: int, tally: int) -> int:
        length = len(seq)
        if length == 0:
            return 0 if tally == 0 else acc
        head, tail = seq[0], seq[1:]
        num = int(head)
        if num % 2 == 1:
            return recurseDigits(tail, acc * num, tally + 1)
        else:
            return recurseDigits(tail, acc, tally)

    return recurseDigits(str(m), 1, 0)