class Solution:
    def maxArea(self, pos_vals, dir_flags):
        height = max(pos_vals) if pos_vals else 0
        m = len(pos_vals)
        greatestSum = 0

        # Convert dir_flags string to list for mutability
        dir_flags = list(dir_flags)

        for _ in range(height * 2):
            for index in range(m):
                if pos_vals[index] == 0 and dir_flags[index] == 'D':
                    dir_flags[index] = 'U'
                elif pos_vals[index] == height and dir_flags[index] == 'U':
                    dir_flags[index] = 'D'

                if dir_flags[index] == 'U':
                    pos_vals[index] += 1
                else:
                    pos_vals[index] -= 1

            tempSum = sum(pos_vals)
            if greatestSum < tempSum:
                greatestSum = tempSum

        return greatestSum