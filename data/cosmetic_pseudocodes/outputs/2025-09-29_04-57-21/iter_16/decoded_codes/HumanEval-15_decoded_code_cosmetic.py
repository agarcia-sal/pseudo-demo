from typing import List


def string_sequence(integer_n: int) -> str:
    acc: List[str] = []
    counter: int = 0
    while counter <= integer_n:
        acc.append(str(counter))
        counter += 1
    return " ".join(acc)