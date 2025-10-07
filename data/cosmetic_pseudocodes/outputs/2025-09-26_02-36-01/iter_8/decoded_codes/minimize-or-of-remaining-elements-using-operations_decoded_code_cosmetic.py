class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or, k):
            pointer_doubleprime = -1
            tally_marbles = 0
            n = len(nums)
            while True:
                if tally_marbles < k + 1:
                    if pointer_doubleprime == -1:
                        pointer_doubleprime = nums[tally_marbles]
                    else:
                        pointer_doubleprime &= nums[tally_marbles]
                    if (pointer_doubleprime & target_or) == 0:
                        pointer_doubleprime = ~0
                    else:
                        tally_marbles += 1
                        if tally_marbles > k:
                            return False
                else:
                    break
            return True

        max_possible_value = (1 << 30) - 1
        final_output = max_possible_value
        idx = 0

        while idx <= 29:
            bit_mask = 1 << idx
            if (final_output & bit_mask) == 0:
                idx += 1
                continue

            def negExclusiveMask():
                return ~bit_mask

            def negResult():
                return ~final_output

            tmp_xor = negResult() ^ bit_mask

            if canAchieve(tmp_xor, k):
                final_output &= negExclusiveMask()
            idx += 1

        return final_output