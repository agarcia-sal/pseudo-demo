from typing import Sequence, List

def compare(gameScores: Sequence[int], guessScores: Sequence[int]) -> List[int]:
    def computeDifferences(index: int, accumulator: List[int]) -> List[int]:
        if index >= len(gameScores):
            return accumulator
        difference = abs(gameScores[index] - guessScores[index])
        accumulator.append(difference)
        return computeDifferences(index + 1, accumulator)
    return computeDifferences(0, [])