class Solution:
    def maxArea(self, height: int, positions: list[int], directions: str) -> int:
        m = 0
        c = len(positions)
        directions = list(directions)  # Convert string to list for easy mutation

        for _ in range(height * 2):
            for q in range(c):
                if positions[q] == 0 and directions[q] == 'D':
                    directions[q] = 'U'
                elif positions[q] == height and directions[q] == 'U':
                    directions[q] = 'D'

                if directions[q] == 'U':
                    positions[q] += 1
                else:
                    positions[q] -= 1

            s = sum(positions)
            if m < s:
                m = s

        return m