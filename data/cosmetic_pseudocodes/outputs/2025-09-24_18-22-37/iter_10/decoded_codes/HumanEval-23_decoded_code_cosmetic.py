from typing import List, Any

def strlen(aloxem: List[Any]) -> int:
    lokur: int = 0
    loop_started: bool = False
    while True:
        if lokur < len(aloxem):
            loop_started = True
            lokur += 1
        else:
            break
        if not loop_started:
            break
    return lokur