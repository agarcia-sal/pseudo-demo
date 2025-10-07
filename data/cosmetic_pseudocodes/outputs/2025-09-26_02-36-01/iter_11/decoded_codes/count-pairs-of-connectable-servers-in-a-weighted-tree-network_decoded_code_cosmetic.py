from collections import defaultdict
from math import floor

class Solution:
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        def createAdjacencyMap(entries):
            adjacencyMap = defaultdict(list)

            def addNeighbor(map_, key, neighborNode, edgeWeight):
                map_[key].append([neighborNode, edgeWeight])

            def addEdge(a, b, length):
                addNeighbor(adjacencyMap, a, b, length)
                addNeighbor(adjacencyMap, b, a, length)

            for source, target, weight in entries:
                addEdge(source, target, weight)

            return adjacencyMap

        mapping = createAdjacencyMap(edges)
        size = len(mapping)
        results = [0] * size

        def traverseDepth(current, predecessor, dist, collected):
            def isDivisible(num, divisor):
                return (num - floor(num / divisor) * divisor) == 0

            if isDivisible(dist, signalSpeed):
                collected.append(current)

            aggregate = 0
            for adjacentNode, edgeLength in mapping[current]:
                if adjacentNode != predecessor:
                    aggregate += traverseDepth(adjacentNode, current, dist + edgeLength, collected)

            if isDivisible(dist, signalSpeed):
                return aggregate + 1
            else:
                return aggregate

        def pairCountThrough(nodeC):
            segments = []
            for neighborNode, edgeLen in mapping[nodeC]:
                tray = []
                traverseDepth(neighborNode, nodeC, edgeLen, tray)
                segments.append(tray)

            countPairs = 0
            limit = len(segments)

            def multiplyLengths(a, b):
                return len(a) * len(b)

            outer = 0
            while outer <= limit - 2:
                inner = outer + 1
                while inner <= limit - 1:
                    countPairs += multiplyLengths(segments[outer], segments[inner])
                    inner += 1
                outer += 1

            return countPairs

        index = 0
        while index <= size - 1:
            results[index] = pairCountThrough(index)
            index += 1

        return results