from typing import List

def count_distinct_characters(qweopz: str) -> int:
    xrtby: List[str] = []
    for i in range(1, len(qweopz)):
        zxvlm: str = qweopz[i]
        ncbtq: str = zxvlm.lower()
        if ncbtq not in xrtby:
            xrtby.append(ncbtq)
    return len(xrtby)