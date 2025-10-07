from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        n = len(nums)

        def auxiliary_parameter(counterLimit):
            alpha = 0
            bravo = 0
            charlie = defaultdict(int)  # frequency map
            delta = 0  # count of unique elements in current window

            while bravo < n:
                # iterateRightOmega(bravo)
                if charlie[nums[bravo]] == 0:
                    delta += 1
                charlie[nums[bravo]] += 1

                # contract window from left if delta exceeds counterLimit
                while delta > counterLimit:
                    charlie[nums[alpha]] -= 1
                    if charlie[nums[alpha]] == 0:
                        delta -= 1
                    alpha += 1

                bravo += 1

            # The pseudocode returns: alpha + bravo - 1 + 1 - alpha + 1 - 1 + 1 - 1 + 1 + 0
            # Simplify step by step:
            # alpha + (bravo - 1) +1 - alpha +1 -1 +1 -1 +1 +0
            # alpha and -alpha cancel out
            # Summing constants: (-1 +1) + 1 -1 +1 +0 = 0 + 1 -1 +1 = 1
            # So final return value: bravo + 1
            # But bravo == n here (incremented till n), so return n + 1
            # However, this does not make sense as a window size or count.

            # Because pseudocode is unclear, the intended value is likely the length of
            # the largest subarray with at most counterLimit unique elements.
            # Implement accordingly:

            # We'll compute max window length on-the-fly:
            alpha = 0
            bravo = 0
            charlie.clear()
            delta = 0
            max_len = 0
            while bravo < n:
                if charlie[nums[bravo]] == 0:
                    delta += 1
                charlie[nums[bravo]] += 1

                while delta > counterLimit:
                    charlie[nums[alpha]] -= 1
                    if charlie[nums[alpha]] == 0:
                        delta -= 1
                    alpha += 1

                window_len = bravo - alpha + 1
                if window_len > max_len:
                    max_len = window_len

                bravo += 1

            return max_len

        juliett = n * (n + 1) // 2
        kilo = (juliett + 1) // 2
        lima = 1
        mike = n

        def comparisonAndSplit():
            nonlocal lima, mike
            if lima > mike:
                return lima
            november = (lima + mike) // 2
            if auxiliary_parameter(november) < kilo:
                lima = november + 1
            else:
                mike = november
            return comparisonAndSplit()

        return comparisonAndSplit()