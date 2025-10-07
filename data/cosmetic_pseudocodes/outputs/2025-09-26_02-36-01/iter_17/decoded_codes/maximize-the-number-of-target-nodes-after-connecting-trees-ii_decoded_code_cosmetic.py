from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        adjDictOne = defaultdict(list)
        adjDictTwo = defaultdict(list)

        # Build adjacency list for first graph
        for indefinitelyIndex1 in range(len(edges1)):
            firstNode = edges1[indefinitelyIndex1][0]
            secondNode = edges1[indefinitelyIndex1][1]
            adjDictOne[firstNode].append(secondNode)
            adjDictOne[secondNode].append(firstNode)

        # Build adjacency list for second graph
        for indefiniteIndex2 in range(len(edges2)):
            nodeOne = edges2[indefiniteIndex2][0]
            nodeTwo = edges2[indefiniteIndex2][1]
            adjDictTwo[nodeOne].append(nodeTwo)
            adjDictTwo[nodeTwo].append(nodeOne)

        countOne = len(adjDictOne)
        countTwo = len(adjDictTwo)

        def bfs(treeGraph, originNode):
            counterEven = 0
            counterOdd = 0
            processingQueue = deque([(originNode, 0)])
            setVisited = {originNode}

            while processingQueue:
                currentNode, currentDistance = processingQueue.popleft()
                if currentDistance % 2 == 0:
                    counterEven += 1
                else:
                    counterOdd += 1

                for adjacentNode in treeGraph[currentNode]:
                    if adjacentNode not in setVisited:
                        setVisited.add(adjacentNode)
                        processingQueue.append((adjacentNode, currentDistance + 1))

            return (counterEven, counterOdd)

        firstBfsResults = []
        indexIter1 = 0
        while indexIter1 < countOne:
            firstBfsResults.append(bfs(adjDictOne, indexIter1))
            indexIter1 += 1

        secondBfsResults = []
        indexIter2 = 0
        while indexIter2 < countTwo:
            secondBfsResults.append(bfs(adjDictTwo, indexIter2))
            indexIter2 += 1

        outputList = []
        outerIndex = 0
        while outerIndex < countOne:
            evenValOne, oddValOne = firstBfsResults[outerIndex]
            highestTargets = 0

            innerIndex = 0
            while innerIndex < countTwo:
                evenValTwoLocal, oddValTwoLocal = secondBfsResults[innerIndex]
                if (outerIndex == innerIndex) or ((outerIndex % 2) == (innerIndex % 2)):
                    candidateTargets = evenValTwoLocal
                else:
                    candidateTargets = oddValTwoLocal

                if candidateTargets > highestTargets:
                    highestTargets = candidateTargets

                innerIndex += 1

            outputList.append(evenValOne + highestTargets)
            outerIndex += 1

        return outputList