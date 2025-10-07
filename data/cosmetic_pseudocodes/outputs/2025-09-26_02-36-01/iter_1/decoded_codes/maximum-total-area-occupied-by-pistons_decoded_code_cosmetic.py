class Solution:
    def maxArea(self, height, positions, directions):
        n = len(positions)
        max_area = sum(positions)
        directions = list(directions)  # convert string to list for mutability
        for _ in range(height * 2):
            for i in range(n):
                if positions[i] == 0 and directions[i] == 'D':
                    directions[i] = 'U'
                elif positions[i] == height and directions[i] == 'U':
                    directions[i] = 'D'
                if directions[i] == 'U':
                    positions[i] += 1
                else:
                    positions[i] -= 1
            current_area = sum(positions)
            if current_area > max_area:
                max_area = current_area
        return max_area