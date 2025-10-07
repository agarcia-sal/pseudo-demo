from math import floor
from typing import List, Dict, Tuple

class Hashing:
    def __init__(self, s: List[str], base: int, mod: int):
        self.mod = mod
        lengthVar = len(s)
        self.h = [0] * (lengthVar + 1)
        self.p = [1] * (lengthVar + 1)

        def computeIndex(counter):
            return counter

        counterVar = 1
        while counterVar <= lengthVar:
            prevIndex = computeIndex(counterVar - 1)
            currIndex = computeIndex(counterVar)

            tempSum = (self.h[prevIndex] * base) + ord(s[prevIndex])
            tempMod = tempSum - (self.mod * (tempSum // self.mod))
            self.h[currIndex] = tempMod

            tempProd = self.p[prevIndex] * base
            prodMod = tempProd - (self.mod * (tempProd // self.mod))
            self.p[currIndex] = prodMod

            counterVar += 1

    def query(self, l: int, r: int) -> int:
        diffVal = self.h[r] - (self.h[l - 1] * self.p[r - l + 1])
        adjustedDiff = diffVal - (self.mod * (diffVal // self.mod))
        return adjustedDiff

class Solution:
    def findAnswer(self, parent: List[int], s: List[str]) -> List[bool]:
        nVal = len(s)
        graph: List[List[int]] = [[] for _ in range(nVal)]

        dfsStrList: List[str] = []
        posDict: Dict[int, Tuple[int, int]] = {}

        def generateDFS(indexVal: int):
            leftPos = len(dfsStrList) + 1
            for currentChild in graph[indexVal]:
                generateDFS(currentChild)
            dfsStrList.append(s[indexVal])
            rightPos = len(dfsStrList)
            posDict[indexVal] = (leftPos, rightPos)

        iterationIndex = 1
        while iterationIndex < nVal:
            parIndex = parent[iterationIndex]
            graph[parIndex].append(iterationIndex)
            iterationIndex += 1

        generateDFS(0)

        baseConst = 33000 + 331
        modVal = 998000000 + 244353

        hashForward = Hashing(dfsStrList, baseConst, modVal)

        def reverseList(origList: List[str]) -> List[str]:
            return origList[::-1]

        reversedDFS = reverseList(dfsStrList)
        hashBackward = Hashing(reversedDFS, baseConst, modVal)

        def isEven(num: int) -> bool:
            return (num % 2) == 0

        answerList: List[bool] = []

        indexIter = 0
        while indexIter < nVal:
            pairLeft, pairRight = posDict[indexIter]
            segmentLength = (pairRight - pairLeft) + 1

            if isEven(segmentLength):
                firstHalfEnd = pairLeft + (segmentLength // 2) - 1
                vA = hashForward.query(pairLeft, firstHalfEnd)
                revStart = nVal - pairRight + 1
                revEnd = revStart + (segmentLength // 2) - 1
                vB = hashBackward.query(revStart, revEnd)
            else:
                firstHalfEnd = pairLeft + (segmentLength // 2) - 1
                vA = hashForward.query(pairLeft, firstHalfEnd)
                revStart = nVal - pairRight + 1
                revEnd = revStart + (segmentLength // 2) - 1
                vB = hashBackward.query(revStart, revEnd)

            isEqual = (vA == vB)
            answerList.append(isEqual)

            indexIter += 1

        return answerList