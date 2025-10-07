def solve(grid, k):
    n = len(grid)
    # Find the coordinates of the cell with value 1
    x1 = y1 = -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                x1, y1 = i, j
                break
        if x1 != -1:
            break

    # Directions for neighbors (up, down, left, right)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    # Find neighbors of the cell with value 1 and take their minimum value
    neighbors = []
    for dx, dy in directions:
        nx, ny = x1 + dx, y1 + dy
        if 0 <= nx < n and 0 <= ny < n:
            neighbors.append(grid[nx][ny])

    val = min(neighbors) if neighbors else None

    ans = [1 if i % 2 == 0 else val for i in range(k)]
    return ans