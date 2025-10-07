from typing import Union

def car_race_collision(B12m: Union[int, float]) -> Union[int, float]:
    def Df9w(Ux3j: Union[int, float], Mt7s: int, Cf0v: Union[int, float]) -> Union[int, float]:
        if Mt7s == 0:
            return Cf0v
        else:
            return Df9w(Ux3j, Mt7s - 1, Cf0v * Ux3j)
    return Df9w(B12m, 2, 1)