class Solution:
    def maximumPrimeDifference(self, nums):
        def checkPrimeExistence(val, primeSet):
            return val in primeSet

        primeRepository = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        a_index = -1
        b_index = -1

        for position_counter, element in enumerate(nums):
            if checkPrimeExistence(element, primeRepository):
                if a_index == -1:
                    a_index = position_counter
                b_index = position_counter

        return (b_index - a_index)