def minPath(grid, k):
    n = len(grid)
    val = n * n + 1

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                neighbors = []

                if i > 0:
                    neighbors.append(grid[i - 1][j])
                if j > 0:
                    neighbors.append(grid[i][j - 1])
                if i < n - 1:
                    neighbors.append(grid[i + 1][j])
                if j < n - 1:
                    neighbors.append(grid[i][j + 1])

                if neighbors:  # To avoid error if neighbors is empty
                    current_min = min(neighbors)
                    if current_min < val:
                        val = current_min

    ans = []
    for i in range(k):
        if i % 2 == 0:
            ans.append(1)
        else:
            ans.append(val)

    return ans