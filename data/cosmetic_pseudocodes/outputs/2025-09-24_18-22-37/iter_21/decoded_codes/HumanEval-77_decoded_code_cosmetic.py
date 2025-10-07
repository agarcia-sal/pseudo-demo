from typing import Union

def iscube(param: Union[int, float]) -> bool:
    val: float = param
    if val < 0:
        val = -val

    temp: float = val
    root_est: int = round(temp ** (1 / 3))
    cube_check: int = root_est * root_est * root_est

    if cube_check == val:
        return True
    else:
        return False