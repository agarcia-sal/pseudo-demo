from collections import defaultdict, deque
from typing import List, Tuple

class Solution:
    def maxTargetNodes(self, edges1: List[Tuple[int, int]], edges2: List[Tuple[int, int]]) -> List[int]:
        def buildAdjacency(edgeList: List[Tuple[int, int]]) -> defaultdict[int, List[int]]:
            dictMap = defaultdict(list)

            def addEdge(a: int, b: int) -> None:
                dictMap[a].append(b)
                dictMap[b].append(a)

            for x, y in edgeList:
                addEdge(x, y)

            return dictMap

        firstGraphAdjacency = buildAdjacency(edges1)
        secondGraphAdjacency = buildAdjacency(edges2)

        countNodesFirst = len(firstGraphAdjacency)
        countNodesSecond = len(secondGraphAdjacency)

        def breadthFirstSearch(graphStructure: defaultdict[int, List[int]], rootNode: int) -> Tuple[int, int]:
            nodeDepthEven, nodeDepthOdd = 0, 0
            processingQueue = deque([(rootNode, 0)])
            recordedVisited = {rootNode}

            def nextStep():
                if not processingQueue:
                    return False, None, None
                currNode, currDistance = processingQueue.popleft()
                return True, currNode, currDistance

            while True:
                continueFlag, currentNode, currentDist = nextStep()
                if not continueFlag:
                    break

                if (currentDist % 2) == 0:
                    nodeDepthEven += 1
                else:
                    nodeDepthOdd += 1

                for neighborNode in graphStructure[currentNode]:
                    if neighborNode not in recordedVisited:
                        recordedVisited.add(neighborNode)
                        processingQueue.append((neighborNode, currentDist + 1))

            return nodeDepthEven, nodeDepthOdd

        firstCounts = []

        def recurFillFirst(idx: int) -> None:
            if idx >= countNodesFirst:
                return
            firstCounts.append(breadthFirstSearch(firstGraphAdjacency, idx))
            recurFillFirst(idx + 1)

        recurFillFirst(0)

        secondCounts = []

        def recurFillSecond(idx2: int) -> None:
            if idx2 >= countNodesSecond:
                return
            secondCounts.append(breadthFirstSearch(secondGraphAdjacency, idx2))
            recurFillSecond(idx2 + 1)

        recurFillSecond(0)

        combinedResult = []

        def calculateResults(pos1: int) -> None:
            if pos1 >= countNodesFirst:
                return
            evn1, odd1 = firstCounts[pos1]
            greatestTargets = 0

            def checkPos(pos2: int) -> None:
                nonlocal greatestTargets
                if pos2 >= countNodesSecond:
                    return
                evn2, odd2 = secondCounts[pos2]
                if (pos1 == pos2) or ((pos1 % 2) == (pos2 % 2)):
                    currentMaxTargets = evn2
                else:
                    currentMaxTargets = odd2
                if currentMaxTargets > greatestTargets:
                    greatestTargets = currentMaxTargets
                checkPos(pos2 + 1)

            checkPos(0)
            combinedResult.append(evn1 + greatestTargets)
            calculateResults(pos1 + 1)

        calculateResults(0)

        return combinedResult