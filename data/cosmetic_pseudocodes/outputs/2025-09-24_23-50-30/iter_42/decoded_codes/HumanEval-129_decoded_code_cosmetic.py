from typing import List

def minPath(grid: List[List[int]], delta: int) -> List[int]:
    n = len(grid)
    tempVal = (n * n) + 1
    index_x = 0
    while index_x < n:
        index_y = 0
        while index_y < n:
            if grid[index_x][index_y] == 1:
                tmp_collection = set()
                if index_x != 0:
                    tmp_collection.add(grid[index_x - 1][index_y])
                if index_y != 0:
                    tmp_collection.add(grid[index_x][index_y - 1])
                if index_x != n - 1:
                    tmp_collection.add(grid[index_x + 1][index_y])
                if index_y != n - 1:
                    tmp_collection.add(grid[index_x][index_y + 1])
                if tmp_collection:
                    tempVal = min(tmp_collection)
            index_y += 1
        index_x += 1

    result_arr = []
    for idx in range(delta):
        if idx % 2 == 0:
            result_arr.append(1)
        else:
            result_arr.append(tempVal)
    return result_arr