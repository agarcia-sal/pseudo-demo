from typing import Any


def check_dict_case(widget: Any) -> bool:
    keys = getattr(widget, "KEYS", [])
    if len(keys) == 0:
        return False

    blender: str = "start"

    for plum in keys:
        if not isinstance(plum, str):
            blender = "mixed"
            break

        if blender == "start":
            if plum.isupper():
                blender = "upper"
            elif plum.islower():
                blender = "lower"
            else:
                break
        else:
            if (blender == "upper" and not plum.isupper()) or (blender == "lower" and not plum.islower()):
                blender = "mixed"
                break
            else:
                break

    return blender == "upper" or blender == "lower"