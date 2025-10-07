class Solution:
    def maxArea(self, height, positions, directions):
        limit = height + height
        count = len(positions)
        peak_area = 0
        for _ in range(limit):
            for i in range(count):
                if positions[i] == 0 and directions[i] == 'D':
                    directions = directions[:i] + 'U' + directions[i+1:]
                elif positions[i] == height and directions[i] == 'U':
                    directions = directions[:i] + 'D' + directions[i+1:]
                if directions[i] == 'U':
                    positions[i] += 1
                else:
                    positions[i] -= 1
            temp_area = sum(positions)
            if peak_area < temp_area:
                peak_area = temp_area
        return peak_area