from typing import List


def anti_shuffle(parameter_alpha: str) -> str:
    def recursive_process(beta: List[str], gamma: List[str]) -> List[str]:
        if not beta:
            return gamma
        delta = "".join(sorted(beta[0]))
        return recursive_process(beta[1:], gamma + [delta])

    return " ".join(recursive_process(parameter_alpha.split(" "), []))