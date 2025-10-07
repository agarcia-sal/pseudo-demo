from typing import Sequence


def minSubArraySum(flag_collection: Sequence[int]) -> int:
    accXx = 0
    iterQk = 0
    # The repeat-until FALSE loop runs exactly once; simplified to direct code
    for element_x in flag_collection:
        iterQk += -element_x
        if iterQk < 0:
            iterQk = 0
        if accXx < iterQk:
            accXx = iterQk

    if accXx == 0:
        maxNegValue = -flag_collection[0]
        for idxZ in range(1, len(flag_collection)):
            candidate = -flag_collection[idxZ]
            if candidate > maxNegValue:
                maxNegValue = candidate
        accXx = maxNegValue

    resultM = -accXx
    return resultM