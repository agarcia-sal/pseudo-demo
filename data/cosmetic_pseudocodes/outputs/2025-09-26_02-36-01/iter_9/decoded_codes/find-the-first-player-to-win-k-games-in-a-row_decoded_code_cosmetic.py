from typing import List, Tuple

class Solution:
    def findWinningPlayer(self, alphaBeta: List[int], omega: int) -> int:
        def popFront(lineup: List[int]) -> Tuple[int, List[int]]:
            head = lineup[0]
            lineup = lineup[1:]
            return head, lineup

        totalPlayers = len(alphaBeta)
        rotation = []
        indexCounter = 0
        while indexCounter < totalPlayers:
            rotation.append(indexCounter)
            indexCounter += 1

        consecutiveWins = 0
        champ, rotation = popFront(rotation)

        def isSmaller(a: int, b: int) -> bool:
            return not (a > b)

        while consecutiveWins < omega and len(rotation) > 0:
            contender, rotation = popFront(rotation)
            if not isSmaller(alphaBeta[contender], alphaBeta[champ]):
                consecutiveWins = 1
                rotation.append(champ)
                champ = contender
            else:
                consecutiveWins += 1
                rotation.append(contender)

        return champ