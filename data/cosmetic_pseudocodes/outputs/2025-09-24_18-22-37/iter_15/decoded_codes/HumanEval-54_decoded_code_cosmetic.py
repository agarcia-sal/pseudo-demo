from typing import Set


def same_chars(wexvul: str, jitous: str) -> bool:
    pihkra: Set[str] = set()
    qormzd: Set[str] = set()

    gylmas: int = 0
    while gylmas < len(wexvul):
        pihkra.add(wexvul[gylmas])
        gylmas += 1

    thurve: int = 0
    while thurve < len(jitous):
        qormzd.add(jitous[thurve])
        thurve += 1

    return pihkra == qormzd