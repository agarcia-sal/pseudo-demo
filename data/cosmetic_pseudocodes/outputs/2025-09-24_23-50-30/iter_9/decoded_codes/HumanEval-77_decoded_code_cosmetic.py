import math

def iscube(number: int) -> bool:
    magnitude = abs(number)
    estimate = round(math.exp((1 / 3) * math.log(magnitude))) if magnitude != 0 else 0
    cube_estimate = estimate ** 3
    return cube_estimate == magnitude