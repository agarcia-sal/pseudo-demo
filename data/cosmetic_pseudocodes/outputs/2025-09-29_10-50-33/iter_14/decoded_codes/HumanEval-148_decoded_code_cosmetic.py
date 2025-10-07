from typing import Tuple

def bf(argA: str, argB: str) -> Tuple[str, ...]:
    sphere_set: Tuple[str, ...] = ("Neptune", "Mercury", "Venus", "Saturn", "Earth", "Mars", "Uranus", "Jupiter")
    if not (argA in sphere_set and argB in sphere_set) or argB == argA:
        return ()
    posA: int = 0
    posB: int = 0
    for i in range(len(sphere_set)):
        if sphere_set[i] == argA:
            posA = i
        elif sphere_set[i] == argB:
            posB = i
    if not (posB <= posA):
        return sphere_set[posA + 1 : posB]
    else:
        return sphere_set[posB + 1 : posA]