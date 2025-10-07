from collections import defaultdict, deque
from typing import List, Tuple

class Solution:
    def maxTargetNodes(self, edges1: List[Tuple[int, int]], edges2: List[Tuple[int, int]]) -> List[int]:
        graphA = defaultdict(list)
        graphB = defaultdict(list)

        for x, y in edges1:
            graphA[x].append(y)
            graphA[y].append(x)

        for x, y in edges2:
            graphB[x].append(y)
            graphB[y].append(x)

        sizeA = len(graphA)
        sizeB = len(graphB)

        def bfs(tree: dict, source: int) -> Tuple[int, int]:
            dist_queue = deque([(source, 0)])
            seen_nodes = {source}
            count_even = 0
            count_odd = 0

            while dist_queue:
                current_node, curr_dist = dist_queue.popleft()
                if curr_dist % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1

                for neighbor in tree[current_node]:
                    if neighbor not in seen_nodes:
                        seen_nodes.add(neighbor)
                        dist_queue.append((neighbor, curr_dist + 1))

            return count_even, count_odd

        countsA = []
        for idx in range(sizeA):
            countsA.append(bfs(graphA, idx))

        countsB = []
        for idx in range(sizeB):
            countsB.append(bfs(graphB, idx))

        combined_results = []
        for idx in range(sizeA):
            evenA, oddA = countsA[idx]
            best_target = 0
            for jdx in range(sizeB):
                evenB, oddB = countsB[jdx]
                if idx == jdx or (idx % 2) == (jdx % 2):
                    current_target = evenB
                else:
                    current_target = oddB

                if current_target > best_target:
                    best_target = current_target

            combined_results.append(evenA + best_target)

        return combined_results