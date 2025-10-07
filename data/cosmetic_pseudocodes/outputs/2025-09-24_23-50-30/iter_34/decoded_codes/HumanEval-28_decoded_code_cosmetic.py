from typing import Iterator, Iterable

def concatenate(widget: Iterable[str]) -> str:
    alpha = ""
    beta: Iterator[str] = iter(widget)
    while True:
        try:
            gamma = next(beta)
        except StopIteration:
            break
        alpha += gamma
    return alpha