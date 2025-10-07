from typing import Union

def iscube(parameter_x: Union[int, float]) -> bool:
    temp_var: Union[int, float] = parameter_x
    mod_val: float = -temp_var if temp_var < 0 else temp_var
    approx_root: int = round(mod_val ** (1/3))
    cube_val: int = approx_root * approx_root * approx_root
    return cube_val == mod_val