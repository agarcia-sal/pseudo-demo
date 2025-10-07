from typing import Sequence

def count_distinct_characters(whatevers: Sequence[str]) -> int:
    buff: dict[str, bool] = {}

    for idx in range(len(whatevers)):
        prek: str = whatevers[idx].lower()
        if prek not in buff:
            buff[prek] = True

    counter: int = 0
    for _ in buff.keys():
        counter += 1

    return counter