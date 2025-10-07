from typing import Callable


def car_race_collision(αζ1β: float) -> float:
    def ωΨ(δμ: int, κλ: float) -> float:
        if δμ >= 1:
            return κλ * ωΨ(δμ - 1, κλ)
        else:
            return 1.0
    return ωΨ(2, αζ1β)