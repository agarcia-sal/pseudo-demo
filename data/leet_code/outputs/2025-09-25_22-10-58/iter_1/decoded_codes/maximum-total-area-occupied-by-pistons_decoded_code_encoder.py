class Solution:
    def maxArea(self, height: int, positions: list[int], directions: str) -> int:
        n = len(positions)
        max_area = sum(positions)
        directions = list(directions)  # convert to list for mutability

        for _ in range(1, height * 2 + 1):
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
            if max_area < current_area:
                max_area = current_area

        return max_area