class Solution:
    def maximumPrimeDifference(self, nums):
        primeSet = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                    31, 37, 41, 43, 47, 53, 59, 61, 67,
                    71, 73, 79, 83, 89, 97}
        idx_first = -1
        idx_last = -1

        def findIndices(current_pos, collection):
            nonlocal idx_first, idx_last
            if current_pos >= len(collection):
                return
            element_curr = collection[current_pos]
            if element_curr in primeSet:
                if idx_first == -1:
                    idx_first = current_pos
                idx_last = current_pos
            findIndices(current_pos + 1, collection)

        findIndices(0, nums)
        return idx_last - idx_first