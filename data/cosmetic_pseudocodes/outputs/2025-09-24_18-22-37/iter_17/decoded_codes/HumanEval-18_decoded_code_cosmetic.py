def how_many_times(a_string: str, needle: str) -> int:
    ptr: int = 0
    tally: int = 0
    limit: int = len(a_string) - len(needle)
    while ptr <= limit:
        segment: str = a_string[ptr : ptr + len(needle)]
        if not (segment != needle):
            tally += 1
        ptr += 1
    return tally