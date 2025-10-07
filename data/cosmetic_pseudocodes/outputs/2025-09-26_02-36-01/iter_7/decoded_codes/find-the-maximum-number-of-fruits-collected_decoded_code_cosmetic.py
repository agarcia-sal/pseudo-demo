class Solution:
    def maxCollectedFruits(self, fruits):
        length_fruits = len(fruits)
        directions_A = [(1, 1), (1, 0)]
        directions_B = [(1, -1), (1, 0), (1, 1)]
        directions_C = [(-1, 1), (0, 1), (1, 1)]
        cache_storage = {}

        def recursiveSearch(posX1, posY1, posX2, posY2, posX3, posY3):
            # Boundary checks for all three positions
            if (posX1 < 0 or posX1 >= length_fruits or posY1 < 0 or posY1 >= length_fruits or
                posX2 < 0 or posX2 >= length_fruits or posY2 < 0 or posY2 >= length_fruits or
                posX3 < 0 or posX3 >= length_fruits or posY3 < 0 or posY3 >= length_fruits):
                return -(1 << 30)  # Large negative number as invalid path marker

            # Check if reached the target cell (bottom-right)
            if (posX1 == posY1 == posX2 == posY2 == posX3 == posY3 == length_fruits - 1):
                return fruits[length_fruits - 1][length_fruits - 1]

            key_tuple = (posX1, posY1, posX2, posY2, posX3, posY3)
            if key_tuple in cache_storage:
                return cache_storage[key_tuple]

            sum_collected = fruits[posX1][posY1]

            # Handle overlapping positions as per original pseudocode logic
            if (posX1 == posX2 and posY1 == posY2) or (posX1 == posX3 and posY1 == posY3):
                sum_collected = 0  # 0 * 2 is 0, thus resetting sum_collected to 0 if overlap with pos1
            if posX2 == posX3 and posY2 == posY3:
                sum_collected += fruits[posX2][posY2]
            else:
                sum_collected += fruits[posX2][posY2] + fruits[posX3][posY3]

            max_additional = -(1 << 30)
            for delta1X, delta1Y in directions_A:
                for delta2X, delta2Y in directions_B:
                    for delta3X, delta3Y in directions_C:
                        candidate_value = recursiveSearch(
                            posX1 + delta1X, posY1 + delta1Y,
                            posX2 + delta2X, posY2 + delta2Y,
                            posX3 + delta3X, posY3 + delta3Y
                        )
                        if candidate_value > max_additional:
                            max_additional = candidate_value

            result_total = sum_collected + max_additional
            cache_storage[key_tuple] = result_total
            return result_total

        # Initial call with positions as specified in pseudocode
        return recursiveSearch(0, 0, 0, length_fruits - 1, length_fruits - 1, 0)