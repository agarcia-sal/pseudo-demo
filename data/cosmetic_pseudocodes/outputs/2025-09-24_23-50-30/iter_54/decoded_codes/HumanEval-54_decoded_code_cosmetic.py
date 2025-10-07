from typing import Sequence


def same_chars(inputAlpha: Sequence[str], inputBeta: Sequence[str]) -> bool:
    accumulatorA: list[str] = []
    for eachElement in inputAlpha:
        if eachElement not in accumulatorA:
            accumulatorA.append(eachElement)

    accumulatorB: list[str] = []
    for eachElement in inputBeta:
        if eachElement not in accumulatorB:
            accumulatorB.append(eachElement)

    if len(accumulatorA) != len(accumulatorB):
        return False
    else:
        indexA = 0
        while indexA < len(accumulatorA):
            found = False
            indexB = 0
            while indexB < len(accumulatorB):
                if accumulatorA[indexA] == accumulatorB[indexB]:
                    found = True
                    break
                indexB += 1
            if not found:
                return False
            indexA += 1
        return True