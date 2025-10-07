from collections import defaultdict, deque
from typing import List, Tuple

class Solution:
    def maxTargetNodes(self, edges1: List[Tuple[int, int]], edges2: List[Tuple[int, int]]) -> List[int]:
        graphA = defaultdict(list)
        graphB = defaultdict(list)

        index1 = 0
        while index1 < len(edges1):
            u1, v1 = edges1[index1]
            graphA[u1].append(v1)
            graphA[v1].append(u1)
            index1 += 1

        index2 = 0
        while index2 < len(edges2):
            x, y = edges2[index2]
            graphB[x].append(y)
            graphB[y].append(x)
            index2 += 1

        sizeA = len(graphA)
        sizeB = len(graphB)

        def bfs(tree: defaultdict, root: int) -> Tuple[int, int]:
            evenLevel = 0
            oddLevel = 0
            container = deque([(root, 0)])
            processed = {root}
            while container:
                currentNode, currentDist = container.popleft()
                if (currentDist & 1) == 0:
                    evenLevel += 1
                else:
                    oddLevel += 1
                for adjNode in tree[currentNode]:
                    if adjNode not in processed:
                        processed.add(adjNode)
                        container.append((adjNode, currentDist + 1))
            return evenLevel, oddLevel

        resultsA = []
        idxA = 0
        while idxA < sizeA:
            resultsA.append(bfs(graphA, idxA))
            idxA += 1

        resultsB = []
        idxB = 0
        while idxB < sizeB:
            resultsB.append(bfs(graphB, idxB))
            idxB += 1

        finalResults = []

        posA = 0
        while posA < sizeA:
            eCountA, oCountA = resultsA[posA]
            maxVal = 0
            posB = 0
            while posB < sizeB:
                eCountB, oCountB = resultsB[posB]
                sameParity = (posA % 2) == (posB % 2)
                if posA == posB or sameParity:
                    candidate = eCountB
                else:
                    candidate = oCountB
                if candidate > maxVal:
                    maxVal = candidate
                posB += 1
            finalResults.append(eCountA + maxVal)
            posA += 1

        return finalResults