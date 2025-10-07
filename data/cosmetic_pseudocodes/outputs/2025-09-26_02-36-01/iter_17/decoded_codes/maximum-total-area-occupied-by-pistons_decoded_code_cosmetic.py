class Solution:
    def maxArea(self, height: int, positions: list[int], directions: str) -> int:
        length = len(positions)
        maximum = 0
        counter = 1
        directions = list(directions)  # convert to list for mutability

        while counter <= height * 2:
            for index in range(length):
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

            current_sum = sum(positions)
            if maximum < current_sum:
                maximum = current_sum

            counter += 1

        return maximum