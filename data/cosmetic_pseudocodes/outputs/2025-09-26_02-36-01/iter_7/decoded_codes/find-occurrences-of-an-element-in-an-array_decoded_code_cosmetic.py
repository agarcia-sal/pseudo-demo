class Solution:
    def occurrencesOfElement(self, nums, queries, x):
        accIndices = []
        idxCounter = 0

        while idxCounter < len(nums):
            currElement = nums[idxCounter]
            if currElement == x:
                accIndices.append(idxCounter)
            idxCounter += 1

        resultSet = []
        queryPointer = 0

        while True:
            if queryPointer > len(queries) - 1:
                break

            currentQuery = queries[queryPointer]
            if currentQuery <= len(accIndices):
                selectedIndex = accIndices[currentQuery - 1]
                resultSet.append(selectedIndex)
            else:
                resultSet.append(-1)

            queryPointer += 1

        return resultSet