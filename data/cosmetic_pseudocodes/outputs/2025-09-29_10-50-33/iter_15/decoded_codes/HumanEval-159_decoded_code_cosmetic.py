from typing import Tuple, Union


def eat(amountTotal: int, requirement: int, leftoverAmount: int) -> Tuple[int, Union[int, bool]]:
    while True:
        if not (requirement > leftoverAmount):
            accumulator: int = amountTotal + requirement
            difference: int = leftoverAmount - requirement
            return accumulator, difference

        accumulator = amountTotal + leftoverAmount
        difference = False
        return accumulator, difference