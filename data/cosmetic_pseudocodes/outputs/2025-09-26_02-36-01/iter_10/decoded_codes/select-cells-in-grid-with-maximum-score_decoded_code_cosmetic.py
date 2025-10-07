class Solution:
    def maxScore(self, grid):
        # Sort each row of grid in descending order using recursive bubble sort
        def sortDescending(arr):
            n = len(arr)

            def swap(i, j):
                arr[i], arr[j] = arr[j], arr[i]

            def bubblePass(i):
                if i == n - 1:
                    return
                if arr[i] < arr[i + 1]:
                    swap(i, i + 1)
                bubblePass(i + 1)

            def fullSort(p):
                if p == 0:
                    return
                bubblePass(0)
                fullSort(p - 1)

            fullSort(n)

        def iterSort(i):
            if i == len(grid):
                return
            sortDescending(grid[i])
            iterSort(i + 1)

        iterSort(0)

        max_sum = 0

        def helper(currRow, taken, aggSum):
            nonlocal max_sum
            if currRow == len(grid):
                if aggSum > max_sum:
                    max_sum = aggSum
                return

            # Case: skip this row
            helper(currRow + 1, taken, aggSum)

            def processIndex(idx):
                if idx == len(grid[currRow]):
                    return
                val = grid[currRow][idx]
                if val not in taken:
                    taken.add(val)
                    helper(currRow + 1, taken, aggSum + val)
                    taken.remove(val)
                processIndex(idx + 1)

            processIndex(0)

        helper(0, set(), 0)
        return max_sum