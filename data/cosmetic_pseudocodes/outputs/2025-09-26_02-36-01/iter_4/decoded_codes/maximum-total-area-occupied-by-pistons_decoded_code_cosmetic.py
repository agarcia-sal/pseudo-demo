class Solution:
    def maxArea(self, height, positions, directions):
        length_positions = len(positions)
        maximum_area = sum(positions)
        directions = list(directions)

        iteration_count = 1
        while iteration_count <= height * 2:
            index = 0
            while index < length_positions:
                pos_value = positions[index]
                dir_char = directions[index]

                if pos_value == 0 and dir_char == 'D':
                    directions[index] = 'U'
                elif pos_value == height and dir_char == 'U':
                    directions[index] = 'D'

                if directions[index] == 'U':
                    positions[index] += 1
                else:
                    positions[index] -= 1

                index += 1

            current_sum = sum(positions)
            if maximum_area < current_sum:
                maximum_area = current_sum

            iteration_count += 1

        return maximum_area