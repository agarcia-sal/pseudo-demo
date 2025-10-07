from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    length: int = len(grid)
    limit: int = length * length + 1

    for index_i in range(length):
        for index_j in range(length):
            if grid[index_i][index_j] == 1:
                temp_values: List[int] = []
                if index_i > 0:
                    temp_values.append(grid[index_i - 1][index_j])
                if index_j > 0:
                    temp_values.append(grid[index_i][index_j - 1])
                if index_i < length - 1:
                    temp_values.append(grid[index_i + 1][index_j])
                if index_j < length - 1:
                    temp_values.append(grid[index_i][index_j + 1])
                if temp_values:
                    limit = min(limit, min(temp_values))

    result_collection: List[int] = []
    for counter_x in range(k):
        if counter_x % 2 == 0:
            result_collection.append(1)
        else:
            result_collection.append(limit)
    return result_collection