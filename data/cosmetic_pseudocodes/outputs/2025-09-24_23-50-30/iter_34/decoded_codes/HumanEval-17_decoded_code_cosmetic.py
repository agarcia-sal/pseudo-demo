from typing import List

def parse_music(xr: str) -> List[int]:
    kp = {"o": 4, "o|": 2, ".|": 1}
    yq: List[int] = []
    zl = xr.split(" ")
    for zi in zl:
        if zi != "":
            yq.append(kp[zi])
    return yq