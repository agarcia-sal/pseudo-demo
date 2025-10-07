class Solution:
    def constructGridLayout(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        degreePositions = [-1] * 5
        for i in range(n):
            lengthDegree = len(graph[i])
            degreePositions[lengthDegree] = i

        row = []
        if degreePositions[1] != -1:
            row = [degreePositions[1]]
        elif degreePositions[4] == -1:
            candidate = degreePositions[2]
            for neighbor in graph[candidate]:
                if len(graph[neighbor]) == 2:
                    row = [candidate, neighbor]
                    break
        else:
            current = degreePositions[2]
            row = [current]
            previous = current
            current = graph[current][0]
            while len(graph[current]) > 2:
                row.append(current)
                for neighbor in graph[current]:
                    if neighbor != previous and len(graph[neighbor]) < 4:
                        previous, current = current, neighbor
                        break
            row.append(current)

        answer = [row]
        visited = [False] * n
        steps = n // len(row) - 1
        for _ in range(1, steps + 1):
            for node in row:
                visited[node] = True
            nextRow = []
            for node in row:
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        nextRow.append(neighbor)
                        break
            answer.append(nextRow)
            row = nextRow

        return answer