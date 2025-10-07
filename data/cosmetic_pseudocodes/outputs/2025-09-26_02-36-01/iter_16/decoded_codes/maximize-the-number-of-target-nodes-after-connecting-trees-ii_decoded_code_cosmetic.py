from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        graphA = defaultdict(list)
        graphB = defaultdict(list)

        idx1 = 0
        while idx1 < len(edges1):
            xA, yA = edges1[idx1]
            graphA[xA].append(yA)
            graphA[yA].append(xA)
            idx1 += 1

        idx2 = 0
        while idx2 < len(edges2):
            xB, yB = edges2[idx2]
            graphB[xB].append(yB)
            graphB[yB].append(xB)
            idx2 += 1

        sizeA = len(graphA)
        sizeB = len(graphB)

        def bfs(tree, origin):
            evens = 0
            odds = 0
            fifo = deque([(origin, 0)])
            inspected = {origin}

            while fifo:
                current, depth = fifo.popleft()
                if depth % 2 == 0:
                    evens += 1
                else:
                    odds += 1

                for neighborNode in tree[current]:
                    if neighborNode not in inspected:
                        inspected.add(neighborNode)
                        fifo.append((neighborNode, depth + 1))

            return evens, odds

        distribution1 = []
        index1 = 0
        while index1 < sizeA:
            distribution1.append(bfs(graphA, index1))
            index1 += 1

        distribution2 = []
        index2 = 0
        while index2 < sizeB:
            distribution2.append(bfs(graphB, index2))
            index2 += 1

        answer_OUT = []
        outerIdx = 0
        while outerIdx < sizeA:
            evEven, evOdd = distribution1[outerIdx]
            maxFound = 0
            innerIdx = 0
            while innerIdx < sizeB:
                evEven2, evOdd2 = distribution2[innerIdx]
                if outerIdx == innerIdx or (outerIdx % 2) == (innerIdx % 2):
                    candidateValue = evEven2
                else:
                    candidateValue = evOdd2

                if candidateValue > maxFound:
                    maxFound = candidateValue

                innerIdx += 1

            answer_OUT.append(evEven + maxFound)
            outerIdx += 1

        return answer_OUT