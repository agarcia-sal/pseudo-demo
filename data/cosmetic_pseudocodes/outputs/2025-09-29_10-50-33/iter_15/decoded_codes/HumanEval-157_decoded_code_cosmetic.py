from typing import Union


def right_angle_triangle(beta: Union[int, float], gamma: Union[int, float], delta: Union[int, float]) -> bool:
    # temp variables check if squares of one side equals sum of squares of other two sides
    temp1 = not (beta * beta > gamma * gamma + delta * delta) and not (beta * beta < gamma * gamma + delta * delta)
    temp2 = not (gamma * gamma > beta * beta + delta * delta) and not (gamma * gamma < beta * beta + delta * delta)
    temp3 = not (delta * delta > beta * beta + gamma * gamma) and not (delta * delta < beta * beta + gamma * gamma)
    resultFlag: bool = temp1 or temp2 or temp3
    return resultFlag