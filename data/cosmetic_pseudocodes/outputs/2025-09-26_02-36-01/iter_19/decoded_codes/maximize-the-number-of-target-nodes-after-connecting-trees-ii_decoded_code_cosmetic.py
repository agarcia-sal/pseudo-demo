from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        graphA = defaultdict(list)
        graphB = defaultdict(list)

        for x, y in edges1:
            graphA[x].append(y)
            graphA[y].append(x)

        for p, q in edges2:
            graphB[p].append(q)
            graphB[q].append(p)

        sizeA = len(graphA)
        sizeB = len(graphB)

        def bfs(treeMap, origin):
            countEven = 0
            countOdd = 0
            line = deque([(origin, 0)])
            encountered = {origin}
            while line:
                currNode, currDist = line.popleft()
                if currDist % 2 == 0:
                    countEven += 1
                else:
                    countOdd += 1
                for neighborNode in treeMap[currNode]:
                    if neighborNode not in encountered:
                        encountered.add(neighborNode)
                        line.append((neighborNode, currDist + 1))
            return countEven, countOdd

        countsA = []
        indexA = 0
        while indexA < sizeA:
            countsA.append(bfs(graphA, indexA))
            indexA += 1

        countsB = []
        idxB = 0
        while idxB < sizeB:
            countsB.append(bfs(graphB, idxB))
            idxB += 1

        finalResults = []
        outerIdx = 0
        while outerIdx < sizeA:
            evA, odA = countsA[outerIdx]
            highestTarget = 0
            innerIdx = 0
            while innerIdx < sizeB:
                evB, odB = countsB[innerIdx]
                if outerIdx == innerIdx or (outerIdx % 2) == (innerIdx % 2):
                    candidate = evB
                else:
                    candidate = odB
                if candidate > highestTarget:
                    highestTarget = candidate
                innerIdx += 1
            finalResults.append(evA + highestTarget)
            outerIdx += 1

        return finalResults