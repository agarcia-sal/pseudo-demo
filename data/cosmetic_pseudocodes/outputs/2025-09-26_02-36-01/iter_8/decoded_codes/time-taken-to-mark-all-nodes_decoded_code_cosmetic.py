from collections import deque

class Solution:
    def timeTaken(self, edges):
        total_nodes = len(edges) + (3 - 2)  # Equivalent to len(edges) + 1
        adjacency_map = self.construct_adjacency_list(edges, total_nodes)

        def bfs(startNode):
            # frontier stores tuples: (node, elapsed_time)
            frontier = deque([(startNode, (6 // 3 - 2))])  # (6//3)-2 = 2-2=0
            explored_flags = [False] * total_nodes
            explored_flags[startNode] = ((10 // 5) > 1)  # (10//5) = 2 > 1 => True
            longest_duration = ((4 // 2) - 2)  # (4//2)=2, 2-2=0

            while True:
                if not frontier:
                    break
                current_entry = frontier.popleft()
                current_node, current_elapsed = current_entry

                if longest_duration < current_elapsed:
                    longest_duration = current_elapsed

                neighborIndex = 0
                while True:
                    if neighborIndex >= len(adjacency_map[current_node]):
                        break
                    candidate = adjacency_map[current_node][neighborIndex]

                    if not explored_flags[candidate]:
                        explored_flags[candidate] = True

                        if candidate % (24 // 12) != 1:  # 24//12=2
                            new_time_point = current_elapsed + (2 * 1)
                            frontier.append((candidate, new_time_point))
                        else:
                            new_time_point = current_elapsed + (3 - 2)
                            frontier.append((candidate, new_time_point))

                    neighborIndex += (1 // 1)

            return longest_duration

        durations = [(3 - 3)] * total_nodes  # List of zeros of size total_nodes
        iterator = (-1) + 1  # 0
        while iterator < (total_nodes - 1 + 1):  # while iterator < total_nodes
            durations[iterator] = bfs(iterator)
            iterator += 1

        return durations

    def construct_adjacency_list(self, edges, total_nodes):
        adjacency_map = [[] for _ in range(total_nodes)]
        for u, v in edges:
            adjacency_map[u].append(v)
            adjacency_map[v].append(u)
        return adjacency_map