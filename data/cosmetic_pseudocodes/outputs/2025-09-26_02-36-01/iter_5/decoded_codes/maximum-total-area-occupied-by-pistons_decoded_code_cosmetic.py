class Solution:
    def maxArea(self, height, positions, directions):
        count = len(positions)
        maximum_area = 0
        directions = list(directions)  # Convert to list for mutability

        for _ in range(height * 2):
            for i in range(count):
                if positions[i] == 0 and directions[i] == 'D':
                    directions[i] = 'U'
                elif positions[i] == height and directions[i] == 'U':
                    directions[i] = 'D'

                if directions[i] == 'U':
                    positions[i] += 1
                else:  # directions[i] == 'D'
                    positions[i] -= 1

            sum_current = sum(positions)
            if maximum_area < sum_current:
                maximum_area = sum_current

        return maximum_area