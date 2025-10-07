from typing import Union

def iscube(num: Union[int, float]) -> bool:
    pos_num: float = abs(num)
    cube_root_candidate: int = round(pos_num ** (1 / 3))
    cube_candidate: int = cube_root_candidate ** 3
    return cube_candidate == pos_num