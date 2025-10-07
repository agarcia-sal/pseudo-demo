class Solution:
    def maxArea(self, height, positions, directions):
        total_positions = positions[:]
        count = len(total_positions)
        accumulated_max = 0
        index_outer = 1
        while index_outer <= height + height:
            index_inner = 0
            while index_inner < count:
                is_at_start = (total_positions[index_inner] == 0)
                dir_char = directions[index_inner]
                if is_at_start and dir_char == 'D':
                    directions = directions[:index_inner] + 'U' + directions[index_inner+1:]
                else:
                    is_at_height = (total_positions[index_inner] == height)
                    if is_at_height and dir_char == 'U':
                        directions = directions[:index_inner] + 'D' + directions[index_inner+1:]
                if directions[index_inner] == 'U':
                    total_positions[index_inner] += 1
                else:
                    total_positions[index_inner] -= 1
                index_inner += 1
            area_sum = sum(total_positions)
            if accumulated_max < area_sum:
                accumulated_max = area_sum
            index_outer += 1
        return accumulated_max