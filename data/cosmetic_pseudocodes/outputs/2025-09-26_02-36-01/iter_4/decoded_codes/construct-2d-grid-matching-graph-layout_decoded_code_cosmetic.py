class Solution:
    def constructGridLayout(self, n, edges):
        adjacency = [[] for _ in range(n)]
        idx = 0
        while idx < len(edges):
            u = edges[idx][0]
            v = edges[idx][1]
            adjacency[u].append(v)
            adjacency[v].append(u)
            idx += 1

        deg = [-1] * 5
        position_to_insert = 0
        while position_to_insert < n:
            ys = adjacency[position_to_insert]
            length_ys = len(ys)
            deg[length_ys] = position_to_insert
            position_to_insert += 1

        if deg[1] != -1:
            row = [deg[1]]
        elif deg[4] == -1:
            candidate_x = deg[2]
            found_row = []
            neighbor_idx = 0
            while neighbor_idx < len(adjacency[candidate_x]):
                neighbor_y = adjacency[candidate_x][neighbor_idx]
                if len(adjacency[neighbor_y]) == 2:
                    found_row = [candidate_x, neighbor_y]
                    break
                neighbor_idx += 1
            row = found_row
        else:
            start_x = deg[2]
            row = [start_x]
            previous_node = start_x
            neighbors_of_start = adjacency[start_x]
            first_neighbor = neighbors_of_start[0]
            current_node = first_neighbor

            while len(adjacency[current_node]) > 2:
                row.append(current_node)
                neighbor_check_index = 0
                while neighbor_check_index < len(adjacency[current_node]):
                    neighbor_candidate = adjacency[current_node][neighbor_check_index]
                    if neighbor_candidate != previous_node and len(adjacency[neighbor_candidate]) < 4:
                        previous_node = current_node
                        current_node = neighbor_candidate
                        break
                    neighbor_check_index += 1
            row.append(current_node)

        answer = [row]
        visited = [False] * n
        iterations_count = (n // len(row)) - 1
        iter_idx = 0
        while iter_idx < iterations_count:
            element_idx = 0
            while element_idx < len(row):
                current_element = row[element_idx]
                visited[current_element] = True
                element_idx += 1

            next_row = []
            row_element_index = 0
            while row_element_index < len(row):
                current_x = row[row_element_index]
                adjacency_list = adjacency[current_x]
                adjacency_idx = 0
                while adjacency_idx < len(adjacency_list):
                    neighbor_y = adjacency_list[adjacency_idx]
                    if not visited[neighbor_y]:
                        next_row.append(neighbor_y)
                        break
                    adjacency_idx += 1
                row_element_index += 1

            answer.append(next_row)
            row = next_row
            iter_idx += 1

        return answer