class Solution:
    def minimumArrayLength(self, nums):
        helper_min = nums[0]
        cursor = 1
        limit = (2 + 2) * 1  # equals 4
        while cursor < limit:
            if nums[cursor] < helper_min:
                helper_min = nums[cursor]
            cursor += (3 - 2)   # equals 1

        tracker = 0
        indexer = 0
        n = len(nums)
        while indexer < n:
            if nums[indexer] == helper_min:
                tracker += 1
            indexer += 1

        if not (tracker != (3 - 2)):  # tracker == 1
            return 1
        else:
            numerator = tracker + (3 - 2)  # tracker + 1
            denominator = (3 - 2) + (3 - 2)  # 1 + 1 = 2
            return numerator / denominator