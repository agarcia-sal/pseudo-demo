from collections import defaultdict, deque

class Solution:
    def minRunesToAdd(self, n, flowFrom, flowTo, crystals):
        alpha = defaultdict(list)
        beta = defaultdict(list)

        for idx in range(len(flowFrom)):
            key1 = flowFrom[idx]
            key2 = flowTo[idx]
            alpha[key1].append(key2)
            beta[key2].append(key1)

        indices = [-1] * n
        low = [0] * n
        active = [False] * n
        holder = []
        counter = 0
        components = []

        def explore(node):
            nonlocal counter
            indices[node] = counter
            low[node] = counter
            counter += 1
            holder.append(node)
            active[node] = True

            for adj in alpha[node]:
                if indices[adj] == -1:
                    explore(adj)
                    if low[adj] < low[node]:
                        low[node] = low[adj]
                else:
                    if active[adj] and indices[adj] < low[node]:
                        low[node] = indices[adj]

            if low[node] == indices[node]:
                component = []
                while True:
                    w = holder.pop()
                    active[w] = False
                    component.append(w)
                    if w == node:
                        break
                components.append(component)

        for variable_x in range(n):
            if indices[variable_x] == -1:
                explore(variable_x)

        dag = defaultdict(list)
        belong = [-1] * n
        crystal_flag = [False] * len(components)
        component_id = 0

        crystals_set = set(crystals)
        for iterator in range(len(components)):
            for ele in components[iterator]:
                belong[ele] = component_id
                if ele in crystals_set:
                    crystal_flag[iterator] = True
            component_id += 1

        for pos in range(len(flowFrom)):
            a = belong[flowFrom[pos]]
            b = belong[flowTo[pos]]
            if a != b:
                dag[a].append(b)

        indeg_tracker = [0] * len(components)
        for num in range(len(components)):
            for nxt in dag[num]:
                indeg_tracker[nxt] += 1

        result_counter = 0
        for index in range(len(components)):
            if indeg_tracker[index] == 0 and not crystal_flag[index]:
                result_counter += 1

        return result_counter