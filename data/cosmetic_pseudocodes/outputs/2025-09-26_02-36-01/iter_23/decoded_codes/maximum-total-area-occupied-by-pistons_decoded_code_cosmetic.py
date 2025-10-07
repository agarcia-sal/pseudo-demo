class Solution:
    def maxArea(self, height, positions, directions):
        n = len(positions)
        max_sum = 0
        directions = list(directions)  # convert to list for easy modification

        for _ in range(height * 2):
            def iteratePositions(i=0):
                if i >= n:
                    return
                if positions[i] == 0 and directions[i] == 'D':
                    directions[i] = 'U'
                elif positions[i] == height and directions[i] == 'U':
                    directions[i] = 'D'
                positions[i] += 1 if directions[i] == 'U' else -1
                iteratePositions(i + 1)

            iteratePositions()

            total = 0
            def sumPositions(i=0):
                nonlocal total
                if i >= n:
                    return
                total += positions[i]
                sumPositions(i + 1)

            sumPositions()
            if max_sum < total:
                max_sum = total

        return max_sum