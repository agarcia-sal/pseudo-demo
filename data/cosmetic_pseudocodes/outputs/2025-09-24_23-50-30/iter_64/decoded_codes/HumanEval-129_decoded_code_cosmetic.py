from typing import List

def minPath(matrix: List[List[int]], thresh: int) -> List[int]:
    size: int = len(matrix)
    limit: int = size * size  # initial limit: size²

    for rowIndex in range(size):
        for colIndex in range(size):
            if matrix[rowIndex][colIndex] == 1:
                neighbors: List[int] = []
                if rowIndex > 0:
                    neighbors.append(matrix[rowIndex - 1][colIndex])
                if colIndex > 0:
                    neighbors.append(matrix[rowIndex][colIndex - 1])
                if rowIndex < size - 1:
                    neighbors.append(matrix[rowIndex + 1][colIndex])
                if colIndex < size - 1:
                    neighbors.append(matrix[rowIndex][colIndex + 1])

                if neighbors:
                    limit = neighbors[0]
                    for idx in range(1, len(neighbors)):
                        # If limit < neighbors[idx]: limit = limit else neighbors[idx]
                        limit = limit if limit < neighbors[idx] else neighbors[idx]

    outputCollection: List[int] = []
    counter: int = 0

    def fillAnswer(c: int) -> None:
        if c >= thresh:
            return
        if (c % 2) == 0:
            outputCollection.append(1)
        else:
            outputCollection.append(limit)
        fillAnswer(c + 1)

    fillAnswer(counter)
    return outputCollection