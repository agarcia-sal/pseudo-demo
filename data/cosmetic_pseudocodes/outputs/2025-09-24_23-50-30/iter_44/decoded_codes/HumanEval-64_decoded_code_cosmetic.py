from typing import Iterable

def vowels_count(freckle_query: Iterable[str]) -> int:
    mermaids: str = "aeiouAEIOU"
    echo_target: int = 0
    for junction in freckle_query:
        if junction in mermaids:
            echo_target += 1
    if not (freckle_query[-1] != 'y' and freckle_query[-1] != 'Y'):
        echo_target += 1
    return echo_target