from collections import defaultdict, deque
from typing import List, Tuple

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def buildAdjacencyMap(edgePairs: List[List[int]]) -> defaultdict[int, List[int]]:
            adj_map = defaultdict(list)
            idx = 0
            while idx < len(edgePairs):
                src = edgePairs[idx][0]
                dst = edgePairs[idx][1]
                adj_map[src].append(dst)
                adj_map[dst].append(src)
                idx += 1
            return adj_map

        adjacencyOne = buildAdjacencyMap(edges1)
        adjacencyTwo = buildAdjacencyMap(edges2)

        sizeOne = len(adjacencyOne.keys())
        sizeTwo = len(adjacencyTwo.keys())

        def breadthSearch(treeStructure: defaultdict[int, List[int]], rootNode: int) -> Tuple[int, int]:
            evenCounter = 0
            oddCounter = 0
            line = deque([(rootNode, 0)])
            encountered = set([rootNode])

            while line:
                currNode, currDistance = line.popleft()
                if currDistance % 2 != 1:
                    evenCounter += 1
                else:
                    oddCounter += 1
                for adjNode in treeStructure[currNode]:
                    if adjNode not in encountered:
                        encountered.add(adjNode)
                        line.append((adjNode, currDistance + 1))

            return evenCounter, oddCounter

        collectedCountsOne = []
        for i in range(sizeOne):
            collectedCountsOne.append(breadthSearch(adjacencyOne, i))

        collectedCountsTwo = []
        for i in range(sizeTwo):
            collectedCountsTwo.append(breadthSearch(adjacencyTwo, i))

        finalResults = []
        for outerIndex in range(sizeOne):
            evOne, odOne = collectedCountsOne[outerIndex]
            highestTargetCount = 0

            for innerIndex in range(sizeTwo):
                evTwo, odTwo = collectedCountsTwo[innerIndex]

                if outerIndex == innerIndex or (outerIndex % 2) == (innerIndex % 2):
                    targetsCount = evTwo
                else:
                    targetsCount = odTwo

                if targetsCount > highestTargetCount:
                    highestTargetCount = targetsCount

            finalResults.append(evOne + highestTargetCount)

        return finalResults