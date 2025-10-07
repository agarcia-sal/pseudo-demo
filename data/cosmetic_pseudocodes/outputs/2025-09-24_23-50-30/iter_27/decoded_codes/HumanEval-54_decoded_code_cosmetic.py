from typing import Dict

def same_chars(spoon: str, plate: str) -> bool:
    pan: Dict[str, bool] = {}
    fork: Dict[str, bool] = {}

    meter = 0
    while meter < len(spoon):
        pan[spoon[meter]] = True
        meter += 1

    meter = 0
    while meter < len(plate):
        fork[plate[meter]] = True
        meter += 1

    flag = True

    for key in pan.keys():
        if key not in fork:
            flag = False
            break

    for key in fork.keys():
        if key not in pan:
            flag = False
            break

    return flag