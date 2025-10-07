from collections import defaultdict

class Solution:
    def findAnswer(self, n, edges):
        def makeGraph(mapping):
            def addEdge(a, b, c):
                mapping[a].append((b, c))
                mapping[b].append((a, c))
            idx = 0
            while idx < len(edges):
                e = edges[idx]
                addEdge(e[0], e[1], e[2])
                idx += 1
            return mapping

        connMap = defaultdict(list)
        connMap = makeGraph(connMap)

        infinity = 10 ** 18
        distances = [infinity] * n
        distances[0] = 0  # distances indexed from 0 with node 0 representing node 1 in pseudocode

        # heap implemented as 1-indexed in pseudocode; use 0-indexed for Python and adapt accordingly
        # But as the pseudocode is custom heap functions, replicate that behavior with 1-based indexing
        # We'll simulate 1-based indexing by storing a dummy value at index 0.

        priorityQueue = [(0, 0)]  # (distance, node)
        # We'll implement heap as 1-based by inserting a dummy at 0 to simplify indexing
        heapArr = [None] + priorityQueue  # heapArr[1] = (0,0)

        def pushHeap(entry):
            heapArr.append(entry)
            pos = len(heapArr) - 1

            def siftUp(p):
                if p == 1:
                    return
                parent = p // 2
                if heapArr[parent][0] > heapArr[p][0]:
                    heapArr[parent], heapArr[p] = heapArr[p], heapArr[parent]
                    siftUp(parent)
            siftUp(pos)

        def popHeap():
            def siftDown(p):
                length = len(heapArr) - 1
                smallest = p
                leftChild = 2 * p
                rightChild = 2 * p + 1
                if leftChild <= length and heapArr[leftChild][0] < heapArr[smallest][0]:
                    smallest = leftChild
                if rightChild <= length and heapArr[rightChild][0] < heapArr[smallest][0]:
                    smallest = rightChild
                if smallest != p:
                    heapArr[p], heapArr[smallest] = heapArr[smallest], heapArr[p]
                    siftDown(smallest)

            topElement = heapArr[1]
            heapArr[1] = heapArr[-1]
            heapArr.pop()
            if len(heapArr) > 1:
                siftDown(1)
            return topElement

        def isEmpty(lst):
            return len(lst) <= 1

        while not isEmpty(heapArr):
            current = popHeap()
            distU = current[0]
            nodeU = current[1]
            if distU > distances[nodeU]:
                continue

            def relaxEdges(neighList):
                i = 0
                while i < len(neighList):
                    neighbor = neighList[i]
                    nodeV = neighbor[0]
                    weightUV = neighbor[1]
                    newDist = distU + weightUV
                    if newDist < distances[nodeV]:
                        distances[nodeV] = newDist
                        pushHeap((newDist, nodeV))
                    i += 1
            relaxEdges(connMap[nodeU])

        edgesSet = dict()
        lastIdx = n - 1
        traversalStack = [(lastIdx, distances[lastIdx])]
        visitedFlags = [False] * n

        def popStack(s):
            val = s[-1]
            s.pop()
            return val

        while traversalStack:
            topPair = popStack(traversalStack)
            currNode = topPair[0]
            currDist = topPair[1]
            if visitedFlags[currNode]:
                continue
            visitedFlags[currNode] = True

            neighborsList = connMap[currNode]
            pos = 0
            while pos < len(neighborsList):
                adj = neighborsList[pos]
                nxtNode = adj[0]
                edgeWt = adj[1]

                if currDist == distances[nxtNode] + edgeWt:
                    a = currNode
                    b = nxtNode
                    if a > b:
                        a, b = b, a
                    edgesSet[(a, b)] = True
                    traversalStack.append((nxtNode, distances[nxtNode]))
                pos += 1

        result = []
        posEdge = 0
        while posEdge < len(edges):
            ed = edges[posEdge]
            x = ed[0]
            y = ed[1]
            minV = x
            maxV = y
            if minV > maxV:
                minV, maxV = maxV, minV
            if edgesSet.get((minV, maxV), False):
                result.append(True)
            else:
                result.append(False)
            posEdge += 1

        return result