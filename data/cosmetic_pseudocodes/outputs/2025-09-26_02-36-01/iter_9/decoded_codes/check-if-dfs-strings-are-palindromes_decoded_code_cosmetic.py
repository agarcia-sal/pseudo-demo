class Hashing:
    def __init__(self, strInput, baseVal, modulus):
        self.mod = modulus
        n = len(strInput)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)

        def computeHashAndPower(idx):
            if idx > n:
                return
            prevHash = self.h[idx - 1]
            currCharCode = ord(strInput[idx - 1])
            hashVal = (prevHash * baseVal + currCharCode) % modulus
            self.h[idx] = hashVal

            prevPower = self.p[idx - 1]
            powerVal = (prevPower * baseVal) % modulus
            self.p[idx] = powerVal

            computeHashAndPower(idx + 1)

        computeHashAndPower(1)

    def query(self, leftBound, rightBound):
        diffHash = self.h[rightBound] - (self.h[leftBound - 1] * self.p[rightBound - leftBound + 1]) % self.mod
        if diffHash < 0:
            diffHash += self.mod
        return diffHash % self.mod


class Solution:
    def findAnswer(self, parentList, strVal):
        graphSize = len(strVal)
        adjacency = [[] for _ in range(graphSize)]

        def buildGraph(index):
            if index >= graphSize:
                return
            currentParent = parentList[index]
            if currentParent != -1:
                adjacency[currentParent].append(index)
            buildGraph(index + 1)

        buildGraph(1)

        traversalSequence = []
        positionsMap = {}

        def depthFirstSearch(node):
            leftIdx = len(traversalSequence) + 1

            def visitChildren(childIdxList, pos):
                if pos >= len(childIdxList):
                    return
                depthFirstSearch(childIdxList[pos])
                visitChildren(childIdxList, pos + 1)

            visitChildren(adjacency[node], 0)

            traversalSequence.append(strVal[node])
            rightIdx = len(traversalSequence)
            positionsMap[node] = (leftIdx, rightIdx)

        depthFirstSearch(0)

        baseConst = 33331
        modConst = 998244353
        forwardHasher = Hashing(traversalSequence, baseConst, modConst)

        def reverseList(originalList):
            reversedArr = []
            idx = len(originalList) - 1
            while idx >= 0:
                reversedArr.append(originalList[idx])
                idx -= 1
            return reversedArr

        reversedTraversal = reverseList(traversalSequence)
        backwardHasher = Hashing(reversedTraversal, baseConst, modConst)

        results = []

        def processNode(i):
            if i >= graphSize:
                return

            leftPos, rightPos = positionsMap[i]
            segmentLength = rightPos - leftPos + 1

            def isEven(num):
                return (num % 2) == 0

            value1 = 0
            value2 = 0

            if isEven(segmentLength):
                halfLen = segmentLength // 2
                value1 = forwardHasher.query(leftPos, leftPos + halfLen - 1)
                revStart = graphSize - rightPos + 1
                revEnd = revStart + halfLen - 1
                value2 = backwardHasher.query(revStart, revEnd)
            else:
                halfLen = segmentLength // 2
                value1 = forwardHasher.query(leftPos, leftPos + halfLen - 1)
                revStart = graphSize - rightPos + 1
                revEnd = revStart + halfLen - 1
                value2 = backwardHasher.query(revStart, revEnd)

            results.append(value1 == value2)

            processNode(i + 1)

        processNode(0)

        return results