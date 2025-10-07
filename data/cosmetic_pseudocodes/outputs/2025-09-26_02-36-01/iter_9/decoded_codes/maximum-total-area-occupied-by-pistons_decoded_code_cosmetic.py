class Solution:
    def maxArea(self, height, positions, directions):
        total_count = len(positions)
        maximum = 0
        iteration_counter = 0

        def toggleDir(idx, dirString):
            # Flip direction at idx: 'U' -> 'D' or 'D' -> 'U'
            if dirString[idx] == 'U':
                toggled = dirString[:idx] + 'D' + dirString[idx + 1:]
            else:
                toggled = dirString[:idx] + 'U' + dirString[idx + 1:]
            return toggled

        def sumArray(arr):
            acc = 0
            i = 0
            while i < len(arr):
                acc += arr[i]
                i += 1
            return acc

        # Convert to mutable list since directions is string
        directions = directions  # string, updated via toggleDir

        # positions list is mutable; directions is updated by toggleDir as string
        while iteration_counter < (height * 2):
            pointer = 0
            while pointer < total_count:
                if positions[pointer] == 0 and directions[pointer] == 'D':
                    directions = toggleDir(pointer, directions)
                elif positions[pointer] == height and directions[pointer] == 'U':
                    directions = toggleDir(pointer, directions)

                if directions[pointer] == 'U':
                    positions[pointer] += 1
                else:
                    positions[pointer] -= 1

                pointer += 1

            slab = sumArray(positions)
            if maximum < slab:
                maximum = slab

            iteration_counter += 1

        return maximum