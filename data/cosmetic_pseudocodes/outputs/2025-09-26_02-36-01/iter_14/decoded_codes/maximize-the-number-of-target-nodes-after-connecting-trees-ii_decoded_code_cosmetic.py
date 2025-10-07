from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        mapA = defaultdict(list)
        mapB = defaultdict(list)

        for elemX, elemY in edges1:
            mapA[elemX].append(elemY)
            mapA[elemY].append(elemX)

        for nodeP, nodeQ in edges2:
            mapB[nodeP].append(nodeQ)
            mapB[nodeQ].append(nodeP)

        sizeA = len(mapA)
        sizeB = len(mapB)

        def breadthFirstSearch(graph, origin):
            countEven = 0
            countOdd = 0
            dq = deque([(origin, 0)])
            visited = set([origin])

            while dq:
                currentNode, distanceValue = dq.popleft()
                if distanceValue % 2 == 0:
                    countEven += 1
                else:
                    countOdd += 1

                for adjNode in graph[currentNode]:
                    if adjNode not in visited:
                        visited.add(adjNode)
                        dq.append((adjNode, distanceValue + 1))
            return countEven, countOdd

        resultsListA = [breadthFirstSearch(mapA, i) for i in range(sizeA)]
        resultsListB = [breadthFirstSearch(mapB, i) for i in range(sizeB)]

        finalResults = []
        for posA in range(sizeA):
            currEvenA, currOddA = resultsListA[posA]
            maxVal = 0
            for posB in range(sizeB):
                evenB, oddB = resultsListB[posB]
                if posA == posB or (posA % 2) == (posB % 2):
                    candidate = evenB
                else:
                    candidate = oddB
                if candidate > maxVal:
                    maxVal = candidate
            finalResults.append(currEvenA + maxVal)

        return finalResults