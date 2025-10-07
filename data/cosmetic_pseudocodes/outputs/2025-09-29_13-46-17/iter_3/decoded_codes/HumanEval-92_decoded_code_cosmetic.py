from typing import Union


def any_int(aValueOne: object, bValueTwo: object, cValueThree: object) -> bool:
    if not isinstance(aValueOne, int):
        return False
    if not isinstance(bValueTwo, int):
        return False
    if not isinstance(cValueThree, int):
        return False

    def checkSums(index: int) -> bool:
        if index == 0:
            if aValueOne + bValueTwo == cValueThree:
                return True
            else:
                return checkSums(index + 1)
        elif index == 1:
            if aValueOne + cValueThree == bValueTwo:
                return True
            else:
                return checkSums(index + 1)
        elif index == 2:
            if bValueTwo + cValueThree == aValueOne:
                return True
            else:
                return False
        return False  # fallback, though index should be in [0..2]

    return checkSums(0)