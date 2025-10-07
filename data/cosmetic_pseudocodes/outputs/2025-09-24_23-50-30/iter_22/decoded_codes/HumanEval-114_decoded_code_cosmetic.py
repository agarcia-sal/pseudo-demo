from typing import List


def minSubArraySum(sequence: List[int]) -> int:
    def reduceSum(seq: List[int], idx: int, accSum: int, bestSum: int) -> int:
        if idx >= len(seq):
            return bestSum
        updatedAcc = accSum - seq[idx]
        constrainedAcc = 0 if updatedAcc < 0 else updatedAcc
        newBest = constrainedAcc if constrainedAcc > bestSum else bestSum
        return reduceSum(seq, idx + 1, constrainedAcc, newBest)

    maxSumCandidate = reduceSum(sequence, 0, 0, 0)
    if maxSumCandidate == 0:
        negations = [-x for x in sequence]
        maxNegation = negations[0]
        for element in negations:
            if element > maxNegation:
                maxNegation = element
        maxSumCandidate = maxNegation

    minimumResult = -maxSumCandidate
    return minimumResult