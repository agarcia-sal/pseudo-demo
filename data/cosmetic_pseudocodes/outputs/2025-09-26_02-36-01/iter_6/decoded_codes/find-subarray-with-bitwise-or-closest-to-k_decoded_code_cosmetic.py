class Solution:
    def minimumDifference(self, nums, k):
        length_of_nums = len(nums)
        best_dist = float('inf')

        def loop_over_starts(a):
            nonlocal best_dist
            if a > length_of_nums - 1:
                return
            current_combined = 0

            def loop_over_ends(b, acc):
                nonlocal best_dist
                if b > length_of_nums - 1:
                    return acc
                new_acc = acc | nums[b]
                difference = abs(k - new_acc)
                if difference < best_dist:
                    best_dist = difference
                if difference == 0:
                    return 0
                return loop_over_ends(b + 1, new_acc)

            result_of_inner = loop_over_ends(a, current_combined)
            if result_of_inner == 0:
                return 0
            loop_over_starts(a + 1)

        loop_over_starts(0)
        return best_dist