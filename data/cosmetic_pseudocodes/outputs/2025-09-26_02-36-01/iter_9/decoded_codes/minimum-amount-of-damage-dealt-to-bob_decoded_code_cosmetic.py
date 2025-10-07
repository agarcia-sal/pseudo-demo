from typing import List

class Enemy:
    def __init__(self, alpha: int, beta: int):
        self.damage = alpha
        self.timeTakenDown = beta

class Solution:
    def minDamage(self, omega: int, theta: List[int], sigma: List[int]) -> int:
        def computeCeilDiv(x: int, y: int) -> int:
            return (x + y - 1) // y

        def cmpRatio(left: Enemy, right: Enemy) -> bool:
            return (left.damage * right.timeTakenDown) > (right.damage * left.timeTakenDown)

        totalSum = 0
        outputAccum = 0
        container = []
        idxTemp = 0

        while idxTemp < len(theta):
            totalSum += theta[idxTemp]
            idxTemp += 1

        cursor = 0
        while True:
            if cursor >= len(theta):
                break
            tmpDamage = theta[cursor]
            tmpHealth = sigma[cursor]
            tmpTime = computeCeilDiv(tmpHealth + omega - 1, omega)
            newEnemy = Enemy(tmpDamage, tmpTime)
            container.append(newEnemy)
            cursor += 1

        def bubbleSort(seq: List[Enemy]):
            lengthSeq = len(seq)
            swapped = True
            while swapped:
                swapped = False
                iVar = 1
                while iVar < lengthSeq:
                    if not cmpRatio(seq[iVar - 1], seq[iVar]):
                        seq[iVar - 1], seq[iVar] = seq[iVar], seq[iVar - 1]
                        swapped = True
                    iVar += 1
                lengthSeq -= 1

        bubbleSort(container)

        iterVar = 0
        while iterVar < len(container):
            outputAccum += totalSum * container[iterVar].timeTakenDown
            totalSum -= container[iterVar].damage
            iterVar += 1

        return outputAccum