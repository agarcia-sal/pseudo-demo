from collections import defaultdict

class Solution:
    def maximumSubtreeSize(self, edges, colors):
        graph = defaultdict(list)
        for firstNode, secondNode in edges:
            graph[firstNode].append(secondNode)
            graph[secondNode].append(firstNode)

        max_size = 1

        def dfs(currentNode, parentNode):
            nonlocal max_size
            subtree_count = 1
            all_same_color_children = True

            neighborsList = graph.get(currentNode, [])
            for adjNode in neighborsList:
                if adjNode != parentNode:
                    returnedCount = dfs(adjNode, currentNode)
                    if returnedCount == 0:
                        all_same_color_children = False
                    else:
                        if colors[adjNode] == colors[currentNode]:
                            subtree_count += returnedCount
                        else:
                            all_same_color_children = False

            if all_same_color_children:
                if subtree_count > max_size:
                    max_size = subtree_count
                return subtree_count
            else:
                return 0

        dfs(0, -1)
        return max_size