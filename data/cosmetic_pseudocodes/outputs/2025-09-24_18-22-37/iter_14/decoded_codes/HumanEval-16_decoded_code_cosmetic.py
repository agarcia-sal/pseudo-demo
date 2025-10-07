def count_distinct_characters(zeta: str) -> int:
    tempSet: set[str] = set()
    i: int = 0
    n: int = len(zeta)
    while i < n:
        ch: str = zeta[i].lower()
        tempSet.add(ch)
        i += 1
    distinctCount: int = len(tempSet)
    return distinctCount