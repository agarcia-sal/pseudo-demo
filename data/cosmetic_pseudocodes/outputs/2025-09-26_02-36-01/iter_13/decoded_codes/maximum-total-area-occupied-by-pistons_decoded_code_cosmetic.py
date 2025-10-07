class Solution:
    def maxArea(self, height, positions, directions):
        n = len(positions)

        def sumList(nums):
            def recurseSum(idx, acc):
                if idx >= len(nums):
                    return acc
                return recurseSum(idx + 1, acc + nums[idx])
            return recurseSum(0, 0)

        maxAreaValue = sumList(positions)
        totalSteps = height * 2
        currentStep = 1

        def replaceCharAt(s, idx, newChar):
            if idx < 0 or idx >= len(s):
                return s
            return s[:idx] + newChar + s[idx+1:]

        directions_str = ''.join(directions) if isinstance(directions, list) else directions
        positions = positions[:]  # ensure we have mutable copy

        while currentStep <= totalSteps:
            index = 0
            while index < n:
                if positions[index] == 0 and directions_str[index] == 'd':
                    directions_str = replaceCharAt(directions_str, index, 'u')
                elif positions[index] == height and directions_str[index] == 'u':
                    directions_str = replaceCharAt(directions_str, index, 'd')

                if directions_str[index] == 'u':
                    positions[index] += 1
                else:
                    positions[index] -= 1

                index += 1

            currentArea = sumList(positions)
            if maxAreaValue < currentArea:
                maxAreaValue = currentArea

            currentStep += 1

        return maxAreaValue