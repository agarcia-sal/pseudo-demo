from collections import defaultdict, deque
from typing import List, Tuple

class Solution:
    def maxTargetNodes(self, edges1: List[Tuple[int, int]], edges2: List[Tuple[int, int]]) -> List[int]:
        adjacencyMap1 = defaultdict(list)
        adjacencyMap2 = defaultdict(list)

        for fromNode, toNode in edges1:
            adjacencyMap1[fromNode].append(toNode)
            adjacencyMap1[toNode].append(fromNode)

        for source, dest in edges2:
            adjacencyMap2[source].append(dest)
            adjacencyMap2[dest].append(source)

        size1 = len(adjacencyMap1)
        size2 = len(adjacencyMap2)

        def bfs(treeStructure: dict, origin: int) -> Tuple[int, int]:
            evenOccurrences = 0
            oddOccurrences = 0
            processingQueue = deque([(origin, 0)])
            seenNodes = {origin}

            while processingQueue:
                currentNode, currentDistance = processingQueue.popleft()
                if currentDistance % 2 == 0:
                    evenOccurrences += 1
                else:
                    oddOccurrences += 1

                for adjacentNode in treeStructure[currentNode]:
                    if adjacentNode not in seenNodes:
                        seenNodes.add(adjacentNode)
                        processingQueue.append((adjacentNode, currentDistance + 1))

            return evenOccurrences, oddOccurrences

        counts1 = [bfs(adjacencyMap1, idx) for idx in range(size1)]
        counts2 = [bfs(adjacencyMap2, idx) for idx in range(size2)]

        outputList = []
        for outerIdx in range(size1):
            evenCountFirst, oddCountFirst = counts1[outerIdx]
            bestTargets = 0
            for innerIdx in range(size2):
                evenCountSecond, oddCountSecond = counts2[innerIdx]

                if outerIdx == innerIdx or (outerIdx % 2) == (innerIdx % 2):
                    candidateTargets = evenCountSecond
                else:
                    candidateTargets = oddCountSecond

                if candidateTargets > bestTargets:
                    bestTargets = candidateTargets

            outputList.append(evenCountFirst + bestTargets)

        return outputList