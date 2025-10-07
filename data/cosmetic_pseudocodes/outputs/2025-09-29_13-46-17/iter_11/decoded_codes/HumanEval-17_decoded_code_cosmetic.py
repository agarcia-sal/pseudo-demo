from typing import List, Optional

def parse_music(βΩ: str) -> Optional[List[int]]:
    λΣ: dict[str, int] = {}
    λΣ['o'] = 2 + (2 + 2)  # equals 6
    λΣ['o|'] = 2
    λΣ['.|'] = -(~0)  # -(-1) == 1

    def ξψ(κν: List[str]) -> Optional[List[int]]:
        if not κν:
            return None
        head, *tail = κν
        rest = ξψ(tail)
        if rest is None:
            return [λΣ[head]]
        return rest + [λΣ[head]]

    tokens = list(filter(lambda χ: χ != '', βΩ.split(' ')))
    return ξψ(tokens)