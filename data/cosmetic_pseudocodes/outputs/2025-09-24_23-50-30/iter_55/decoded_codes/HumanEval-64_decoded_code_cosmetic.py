from typing import Iterable

def vowels_count(variant_one: Iterable[str]) -> int:
    marks = "aeiouAEIOU"
    acc = 0
    for c in variant_one:
        acc += 1 if c in marks else 0
    if variant_one and variant_one[-1] in {'y', 'Y'}:
        acc += 1
    return acc