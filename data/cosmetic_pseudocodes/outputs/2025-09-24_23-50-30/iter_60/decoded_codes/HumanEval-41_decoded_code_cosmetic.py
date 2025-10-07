from typing import Any


def car_race_collision(pqr: Any) -> Any:
    def inner_square(stu: Any, vwx: int) -> Any:
        if vwx == 0:
            return 1
        else:
            return stu * inner_square(stu, vwx - 1)
    return inner_square(pqr, 2)