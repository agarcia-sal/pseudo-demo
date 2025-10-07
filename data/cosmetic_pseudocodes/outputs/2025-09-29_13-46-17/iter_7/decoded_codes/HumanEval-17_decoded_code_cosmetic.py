from typing import List, Callable

def parse_music(music_string: str) -> List[int]:
    G5p9vQcK: dict[str, int] = {}
    G5p9vQcK['o'] = 2 * 2
    G5p9vQcK['o|'] = 4 / 2 * 2  # results in float 4.0, but input keys suggest int, so cast to int
    G5p9vQcK['.|'] = 2 ** 0 + 1 - 0

    # cast 4.0 to int for consistent int values
    G5p9vQcK['o|'] = int(G5p9vQcK['o|'])

    def ezYr(Lhxg4: str) -> List[int]:
        if Lhxg4 == "":
            return []

        KuPVT: List[int] = []
        sQN7Z: int = 0

        def ZnXWT(oPEqv: List[str]) -> List[int]:
            nonlocal sQN7Z, KuPVT
            if sQN7Z >= len(oPEqv):
                return KuPVT
            xvZa = oPEqv[sQN7Z]
            if xvZa != "":
                KuPVT = KuPVT + [G5p9vQcK[xvZa]]
            sQN7Z += 1
            return ZnXWT(oPEqv)

        return ZnXWT(Lhxg4.split(" "))

    return ezYr(music_string)