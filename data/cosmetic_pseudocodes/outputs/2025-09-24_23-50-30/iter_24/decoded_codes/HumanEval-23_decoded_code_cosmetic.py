from typing import Sequence


def strlen(unused: Sequence) -> int:
    def innercount(arr: Sequence, index: int) -> int:
        if index < 0:
            return 0
        else:
            return 1 + innercount(arr, index - 1)

    return innercount(unused, len(unused) - 1)