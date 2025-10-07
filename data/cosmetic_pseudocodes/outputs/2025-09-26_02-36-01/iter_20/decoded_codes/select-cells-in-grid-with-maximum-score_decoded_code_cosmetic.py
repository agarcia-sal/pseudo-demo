class Solution:
    def maxScore(self, grid):
        # Sort each row in descending order using bubble sort as per pseudocode
        def customSortDesc(arr):
            def swap(i, j):
                arr[i], arr[j] = arr[j], arr[i]

            i = 0
            while i < len(arr) - 1:
                j = 0
                while j < len(arr) - i - 1:
                    if arr[j] < arr[j + 1]:
                        swap(j, j + 1)
                    j += 1
                i += 1

        for idx in range(len(grid)):
            customSortDesc(grid[idx])

        gamma = 0

        def alpha(mu, phi, omega):
            nonlocal gamma
            if mu >= len(grid):
                beta = omega if gamma < omega else gamma
                gamma = beta
                return
            else:
                alpha(mu + 1, phi, omega)
                delta = 0
                while delta < len(grid[mu]):
                    epsilon = grid[mu][delta]
                    if epsilon not in phi:
                        phi.add(epsilon)
                        alpha(mu + 1, phi, omega + epsilon)
                        phi.remove(epsilon)
                    delta += 1

        alpha(0, set(), 0)
        return gamma