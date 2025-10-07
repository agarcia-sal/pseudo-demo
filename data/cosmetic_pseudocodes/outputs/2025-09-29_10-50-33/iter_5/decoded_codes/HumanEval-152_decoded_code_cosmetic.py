from typing import List

def compare(listScoresGame: List[int], listScoresGuess: List[int]) -> List[int]:
    def absDiff(a: int, b: int) -> int:
        return a - b if a >= b else b - a

    resultCollection: List[int] = []
    index: int = 0

    while index < len(listScoresGame):
        resultCollection.append(absDiff(listScoresGame[index], listScoresGuess[index]))
        index += 1

    return resultCollection