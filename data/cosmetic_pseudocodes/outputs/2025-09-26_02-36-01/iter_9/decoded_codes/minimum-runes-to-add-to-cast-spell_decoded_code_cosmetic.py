from collections import defaultdict, deque

class Solution:

    def minRunesToAdd(self, alpha: int, flowFrom: list[int], flowTo: list[int], gamma: set[int]) -> int:
        graph = defaultdict(list)
        reverseGraph = defaultdict(list)

        def buildGraph():
            def go(xlist, ylist, pos):
                if pos >= len(xlist):
                    return
                graph[xlist[pos]].append(ylist[pos])
                reverseGraph[ylist[pos]].append(xlist[pos])
                go(xlist, ylist, pos + 1)
            go(flowFrom, flowTo, 0)

        buildGraph()

        indices = [-1] * alpha
        lowlinks = [0] * alpha
        onStack = [False] * alpha
        stack = []
        currentIndex = 0
        sccs = []

        def tarjan(node):
            nonlocal currentIndex
            indices[node] = currentIndex
            lowlinks[node] = currentIndex
            currentIndex += 1
            stack.append(node)
            onStack[node] = True

            neighbors = graph[node]
            j = 0
            while j < len(neighbors):
                neighbor = neighbors[j]
                if indices[neighbor] == -1:
                    tarjan(neighbor)
                    if lowlinks[node] > lowlinks[neighbor]:
                        lowlinks[node] = lowlinks[neighbor]
                elif onStack[neighbor]:
                    if lowlinks[node] > indices[neighbor]:
                        lowlinks[node] = indices[neighbor]
                j += 1

            if lowlinks[node] == indices[node]:
                component = []
                while True:
                    w = stack.pop()
                    onStack[w] = False
                    component.append(w)
                    if w == node:
                        break
                sccs.append(component)

        i = 0
        while i < alpha:
            if indices[i] == -1:
                tarjan(i)
            i += 1

        sccGraph = defaultdict(list)
        sccIndex = [-1] * alpha
        ownedByCrystal = [False] * len(sccs)
        countScc = 0

        k = 0
        while k < len(sccs):
            comp = sccs[k]
            m = 0
            while m < len(comp):
                node = comp[m]
                sccIndex[node] = countScc
                if node in gamma:
                    ownedByCrystal[countScc] = True
                m += 1
            countScc += 1
            k += 1

        h = 0
        while h < len(flowFrom):
            sourceScc = sccIndex[flowFrom[h]]
            targetScc = sccIndex[flowTo[h]]
            if sourceScc != targetScc:
                sccGraph[sourceScc].append(targetScc)
            h += 1

        degrees = [0] * len(sccs)

        x = 0
        while x < len(sccs):
            adj = sccGraph[x]
            y = 0
            while y < len(adj):
                pos = adj[y]
                degrees[pos] += 1
                y += 1
            x += 1

        requiredRunes = 0
        q = 0
        while q < len(sccs):
            if degrees[q] == 0 and not ownedByCrystal[q]:
                requiredRunes += 1
            q += 1

        return requiredRunes