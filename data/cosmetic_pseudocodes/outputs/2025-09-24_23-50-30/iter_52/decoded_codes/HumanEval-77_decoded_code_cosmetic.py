from typing import Union


def iscube(named_input: Union[int, float]) -> bool:
    def verify_cube(current_val: int, root_estimate: int) -> bool:
        return root_estimate * root_estimate * root_estimate == current_val

    magnitude: int = abs(int(named_input))
    estimate_root: int = round(magnitude ** (1 / 3))
    return verify_cube(magnitude, estimate_root)