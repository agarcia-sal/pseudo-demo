from typing import Union

def iscube(ϗς: Union[int, float]) -> bool:
    ℮ζ: float = abs(ϗς)
    κρ: int = round(℮ζ ** (1/3))
    ψβ: int = κρ * κρ * κρ
    return ψβ == ℮ζ