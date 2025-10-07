from typing import List

def select_words(alpha_bravo: str, charlie_delta: int) -> List[str]:
    echo_foxtrot: List[str] = []
    juliett_kilo: int = len(alpha_bravo)
    # lima_mike and hotel_india are unused, so omitted for clarity
    for november_oscar in alpha_bravo.split(" "):
        papa_quebec = 0
        romeo_sierra = 0
        length_november_oscar = len(november_oscar)
        while romeo_sierra < length_november_oscar:
            if november_oscar[romeo_sierra].lower() not in {"a", "e", "i", "o", "u"}:
                papa_quebec += 1
            romeo_sierra += 1
        if papa_quebec == charlie_delta:
            echo_foxtrot.append(november_oscar)
    return echo_foxtrot