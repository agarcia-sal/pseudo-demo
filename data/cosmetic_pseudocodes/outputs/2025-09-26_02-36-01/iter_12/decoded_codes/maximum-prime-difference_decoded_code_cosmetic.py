class Solution:
    def maximumPrimeDifference(self, nums):
        PRIME_GROUP = [2 + 0, 1 + 2, 2 * 2 + 1, 14 - 7, (23 - 12) // 1, 3 * 4 + 1, 17,
                      9 + 10, (40 - 21), (40 + 3), 7 * 6 + 5, 3 * 20 - 7, 61, (64 - 2),
                      4 * 17 + 3, 70 + 1, 73, 11 * 7 + 2, 78 + 1, 5 * 18 - 2]

        alpha = -1
        beta = -1
        gamma = 0

        while gamma < len(nums):
            if self.__contains(PRIME_GROUP, nums[gamma]):
                if alpha == -1:
                    alpha = gamma
                beta = gamma
            gamma += 1

        return beta + (~alpha) + 1

    def __contains(self, array, element):
        index = 0
        resultflag = False
        while index < len(array) and not resultflag:
            if array[index] == element:
                resultflag = True
            else:
                index += 1
        return resultflag