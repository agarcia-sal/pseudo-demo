from collections import deque
from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        def explore(nodeIdx: int, parentIdx: int, distanceArray: List[int]) -> None:
            if nodeIdx < 0:
                return
            queueList = [nodeIdx]
            pointerIdx = 0
            while pointerIdx < len(queueList):
                currentNode = queueList[pointerIdx]
                nextNodes = g[currentNode]
                adjIdx = 0
                while adjIdx < len(nextNodes):
                    linkedNode = nextNodes[adjIdx]
                    if linkedNode != parentIdx and distanceArray[linkedNode] < 0:
                        distanceArray[linkedNode] = distanceArray[currentNode] + 1
                        queueList.append(linkedNode)
                    adjIdx += 1
                pointerIdx += 1

        nodeCount = len(edges) + 1
        g = [[] for _ in range(nodeCount)]

        for u_val, v_val in edges:
            g[u_val].append(v_val)
            g[v_val].append(u_val)

        distFromStart = [-1] * nodeCount
        distFromStart[0] = 0
        explore(0, -1, distFromStart)
        maxDistA = distFromStart[0]
        aIndex = 0
        distIter = 1
        while distIter < nodeCount:
            if distFromStart[distIter] > maxDistA:
                maxDistA = distFromStart[distIter]
                aIndex = distIter
            distIter += 1

        distFromA = [-1] * nodeCount
        distFromA[aIndex] = 0
        explore(aIndex, -1, distFromA)
        maxDistB = distFromA[0]
        bIndex = 0
        distIterB = 1
        while distIterB < nodeCount:
            if distFromA[distIterB] > maxDistB:
                maxDistB = distFromA[distIterB]
                bIndex = distIterB
            distIterB += 1

        distFromB = [-1] * nodeCount
        distFromB[bIndex] = 0
        explore(bIndex, -1, distFromB)

        answerList = []
        posIter = 0
        while posIter < nodeCount:
            if distFromA[posIter] > distFromB[posIter]:
                answerList.append(aIndex)
            else:
                answerList.append(bIndex)
            posIter += 1

        return answerList