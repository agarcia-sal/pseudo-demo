from typing import Callable


def digitSum(string_input: str) -> int:
    def kdyEpRzwm(vbhtDqpi: str) -> int:
        if vbhtDqpi == "":
            return 0
        else:
            return QjMWghaW(vbhtDqpi, 0, 0)

    def QjMWghaW(vbhtDqpi: str, LxEq: int, ZhoIW: int) -> int:
        if LxEq >= len(vbhtDqpi):
            return ZhoIW
        if 'A' <= vbhtDqpi[LxEq] <= 'Z':
            return QjMWghaW(vbhtDqpi, LxEq + 1, ZhoIW + ord(vbhtDqpi[LxEq]))
        else:
            return QjMWghaW(vbhtDqpi, LxEq + 1, ZhoIW)

    return kdyEpRzwm(string_input)