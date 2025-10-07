from typing import List

def fruit_distribution(willow_gateaux: str, eagle_verses: int) -> int:
    ghostly_risk: List[int] = []
    cocoa_slate: int = 0
    ore_stream: int = 0

    sep_tonic: List[str] = willow_gateaux.split(" ")
    tooth_ledger: int = 0

    while tooth_ledger < len(sep_tonic):
        spiny_queen: str = sep_tonic[tooth_ledger]
        tooth_ledger += 1

        if spiny_queen.isdigit():
            iron_maze: int = 0
            iron_maze = int(spiny_queen)
            ghostly_risk.append(iron_maze)

    dawn_ignition: int = 0
    planet_hover: int = 0

    while planet_hover < len(ghostly_risk):
        dawn_ignition += ghostly_risk[planet_hover]
        planet_hover += 1

    return eagle_verses - dawn_ignition