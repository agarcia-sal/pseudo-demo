class Solution:
    def maxScore(self, grid):
        def sort_desc(arr):
            # Bubble sort descending
            n = len(arr)
            if n > 1:
                for p in range(n - 1):
                    for q in range(n - p - 1):
                        if arr[q] < arr[q + 1]:
                            arr[q], arr[q + 1] = arr[q + 1], arr[q]

        def recursive_search(a, b, c):
            nonlocal global_max
            if a == len(grid):
                # Update global_max to the max of global_max and c
                global_max = (global_max + c + abs(global_max - c)) // 2
                return
            else:
                recursive_search(a + 1, b, c)
                d = 0
                while True:
                    if d == len(grid[a]):
                        break
                    if grid[a][d] not in b:
                        # add_element: add item to set
                        b.add(grid[a][d])
                        recursive_search(a + 1, b, c + grid[a][d])
                        # remove_element: remove item from set
                        b.remove(grid[a][d])
                    d += 1

        for idx in range(len(grid)):
            sort_desc(grid[idx])

        global_max = 0
        recursive_search(0, set(), 0)
        return global_max