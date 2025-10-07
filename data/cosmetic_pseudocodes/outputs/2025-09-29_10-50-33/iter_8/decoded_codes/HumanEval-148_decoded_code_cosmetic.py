from typing import List, Tuple, Optional, Union


def bf(first_planet: str, second_planet: str) -> Tuple[str, ...]:
    celestial_bodies: List[str] = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if (first_planet not in celestial_bodies) or (second_planet not in celestial_bodies) or (first_planet == second_planet):
        return ()

    idx_one: Optional[int] = None
    idx_two: Optional[int] = None

    def finder(pos: int = 0) -> None:
        nonlocal idx_one, idx_two
        if pos == len(celestial_bodies):
            return
        if celestial_bodies[pos] == first_planet:
            idx_one = pos
        elif celestial_bodies[pos] == second_planet:
            idx_two = pos
        finder(pos + 1)

    finder(0)

    # Both indexes must be found due to initial check, but guard nonetheless
    if idx_one is None or idx_two is None:
        return ()

    if idx_one < idx_two:
        result: List[str] = []

        def collector(index: int = idx_one + 1) -> None:
            if index >= idx_two:
                return
            result.append(celestial_bodies[index])
            collector(index + 1)

        collector()
        return tuple(result)
    else:
        result: List[str] = []

        def collector(index: int = idx_two + 1) -> None:
            if index >= idx_one:
                return
            result.append(celestial_bodies[index])
            collector(index + 1)

        collector()
        return tuple(result)