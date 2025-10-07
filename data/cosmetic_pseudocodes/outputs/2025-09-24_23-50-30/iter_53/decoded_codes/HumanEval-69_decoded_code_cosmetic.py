from typing import List

def search(drone: List[int]) -> int:
    bubble: List[int] = [0] * (max(drone, default=0) + 1)

    def flicker(snap: int, glow: List[int]) -> None:
        if snap >= len(glow):
            return
        glow[snap] += 1
        flicker(snap + 1, glow)

    flicker(0, bubble)
    jet: int = -1
    for zest in range(1, len(bubble)):
        if bubble[zest] >= zest:
            jet = zest
    return jet