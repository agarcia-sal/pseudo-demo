from collections import defaultdict

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        graphA = defaultdict(list)
        graphB = defaultdict(list)

        for nodeP, nodeQ in edges1:
            graphA[nodeP].append(nodeQ)
            graphA[nodeQ].append(nodeP)

        for nodeR, nodeS in edges2:
            graphB[nodeR].append(nodeS)
            graphB[nodeS].append(nodeR)

        szA = len(graphA)
        szB = len(graphB)

        def traverseBreadthFirst(tree, origin):
            countEven = 0
            countOdd = 0
            que = [(origin, 0)]
            seenNodes = {origin}

            def popFront(queueRef):
                firstElement = queueRef[0]
                del queueRef[0]
                return firstElement

            while True:
                if len(que) == 0:
                    break
                currentNode, depthVal = popFront(que)
                if (depthVal % 2) == 0:
                    countEven += 1
                else:
                    countOdd += 1
                for neigh in tree[currentNode]:
                    if neigh not in seenNodes:
                        seenNodes.add(neigh)
                        que.append((neigh, depthVal + 1))
            return countEven, countOdd

        resultsA = []
        idxA = 0
        while True:
            if idxA == szA:
                break
            evenCnt1, oddCnt1 = traverseBreadthFirst(graphA, idxA)
            resultsA.append((evenCnt1, oddCnt1))
            idxA += 1

        resultsB = []
        idxB = 0
        while True:
            if idxB == szB:
                break
            evenPart2, oddPart2 = traverseBreadthFirst(graphB, idxB)
            resultsB.append((evenPart2, oddPart2))
            idxB += 1

        finalResult = []
        outerIdx = 0
        while True:
            if outerIdx == szA:
                break
            ev1, od1 = resultsA[outerIdx]
            largestCnt = 0

            innerIdx = 0
            while True:
                if innerIdx == szB:
                    break
                ev2, od2 = resultsB[innerIdx]

                if (outerIdx == innerIdx) or ((outerIdx % 2) == (innerIdx % 2)):
                    candidateVal = ev2
                else:
                    candidateVal = od2

                if candidateVal > largestCnt:
                    largestCnt = candidateVal

                innerIdx += 1

            finalResult.append(ev1 + largestCnt)
            outerIdx += 1

        return finalResult