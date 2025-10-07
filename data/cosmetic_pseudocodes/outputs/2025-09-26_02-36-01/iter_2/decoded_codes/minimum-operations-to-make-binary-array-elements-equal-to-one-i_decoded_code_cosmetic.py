class Solution:
    def minOperations(self, arr: list[int]) -> int:
        lengthVar = len(arr)
        countOps = 0
        indexVar = 0
        while indexVar <= lengthVar - 3:
            if arr[indexVar] == 0:
                arr[indexVar] = 1 - arr[indexVar]
                arr[indexVar + 1] = 1 - arr[indexVar + 1]
                arr[indexVar + 2] = 1 - arr[indexVar + 2]
                countOps += 1
            indexVar += 1

        if arr[-1] == 0 or arr[-2] == 0:
            return -1
        return countOps