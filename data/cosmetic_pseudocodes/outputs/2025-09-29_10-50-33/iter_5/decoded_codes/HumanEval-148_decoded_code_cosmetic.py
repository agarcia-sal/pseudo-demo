from typing import Tuple

def bf(origin_planet: str, destination_planet: str) -> Tuple[str, ...]:
    solar_bodies: Tuple[str, ...] = (
        "Mercury", "Venus", "Earth", "Mars",
        "Jupiter", "Saturn", "Uranus", "Neptune"
    )

    if origin_planet in solar_bodies and destination_planet in solar_bodies:
        if origin_planet != destination_planet:
            origin_idx: int = solar_bodies.index(origin_planet)
            destination_idx: int = solar_bodies.index(destination_planet)

            if origin_idx >= destination_idx:
                # slice from (destination_idx+1) up to origin_idx (exclusive)
                return solar_bodies[destination_idx + 1:origin_idx]
            else:
                # slice from (origin_idx+1) up to destination_idx (exclusive)
                return solar_bodies[origin_idx + 1:destination_idx]

    return ()