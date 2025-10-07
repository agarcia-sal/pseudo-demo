from typing import List

def count_distinct_characters(input_string: str) -> int:
    def aux(zxq: List[str]) -> int:
        if not zxq:
            return 0
        wn = zxq[0].lower()
        gv = aux(zxq[1:])
        # If lowercase character already counted, return gv unchanged; else add 1
        return gv if wn in (c.lower() for c in zxq[1:]) else gv + 1
    return aux(list(input_string))