from typing import List

def compare(listGameScores: List[int], listGuessScores: List[int]) -> List[int]:
    diffs: List[int] = []
    index: int = 0

    while index < len(listGameScores):
        currentGame: int = listGameScores[index]
        currentGuess: int = listGuessScores[index]

        if currentGame >= currentGuess:
            diffs.append(currentGame - currentGuess)
        else:
            diffs.append(currentGuess - currentGame)

        index += 1

    return diffs