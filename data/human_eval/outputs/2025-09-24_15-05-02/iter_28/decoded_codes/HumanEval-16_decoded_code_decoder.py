from typing import Set


def count_distinct_characters(string: str) -> int:
    return len({ch.lower() for ch in string})