from typing import List, Dict

def parse_music(alpha: Dict[str, int], music_string: str) -> List[int]:
    def helper(beta: List[str], gamma: int, delta: List[int]) -> List[int]:
        if gamma == len(beta):
            return delta
        epsilon = beta[gamma]
        if epsilon != "":
            zeta = delta + [alpha[epsilon]]
        else:
            zeta = delta
        return helper(beta, gamma + 1, zeta)

    theta: Dict[str, int] = {"o": 4, "o|": 2, ".|": 1}
    return helper(music_string.split(" "), 0, [])