from typing import List

class Solution:
	def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
		graph = [[] for _ in range(n)]
		for edge_u, edge_v in edges:
			graph[edge_u].append(edge_v)
			graph[edge_v].append(edge_u)

		degreeList = [-1] * 5
		for idx, neighbors in enumerate(graph):
			if len(neighbors) < 5:
				degreeList[len(neighbors)] = idx

		if degreeList[1] != -1:
			currentRow = [degreeList[1]]
		elif degreeList[4] == -1:
			startNode = degreeList[2]
			currentRow = []
			for candidate in graph[startNode]:
				if len(graph[candidate]) == 2:
					currentRow = [startNode, candidate]
					break
		else:
			startNode = degreeList[2]
			currentRow = [startNode]
			lastNode = startNode
			startNode = graph[startNode][0]
			while len(graph[startNode]) > 2:
				currentRow.append(startNode)
				for neighbor in graph[startNode]:
					if neighbor != lastNode and len(graph[neighbor]) < 3:
						lastNode = startNode
						startNode = neighbor
						break
			currentRow.append(startNode)

		answer = [currentRow]
		visited = [False] * n
		totalIterations = (n // len(currentRow)) - 1

		for _ in range(totalIterations):
			for element_x in currentRow:
				visited[element_x] = True
			nextRow = []
			for element_x in currentRow:
				for neighbor_y in graph[element_x]:
					if not visited[neighbor_y]:
						nextRow.append(neighbor_y)
						break
			answer.append(nextRow)
			currentRow = nextRow

		return answer