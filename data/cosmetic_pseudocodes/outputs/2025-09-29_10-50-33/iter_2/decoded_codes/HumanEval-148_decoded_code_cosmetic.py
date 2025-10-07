from typing import Tuple

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    solar_system: Tuple[str, ...] = (
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    )
    if not (planet1 in solar_system and planet2 in solar_system) or planet1 == planet2:
        return ()
    idx_a = solar_system.index(planet1)
    idx_b = solar_system.index(planet2)
    if idx_a > idx_b:
        return solar_system[idx_b + 1 : idx_a]
    else:
        return solar_system[idx_a + 1 : idx_b]