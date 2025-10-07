class Solution:
    def minChanges(self, nums, k):
        def compute_prefix_sums(arr):
            acc = [0]
            for val in arr:
                acc.append(acc[-1] + val)
            return acc

        delta = [0] * (k + 2)
        total = len(nums)
        pos = 0

        while True:
            if pos >= total // 2:
                break

            elem1 = nums[pos]
            elem2 = nums[-1 - pos]
            a_temp, b_temp = elem1, elem2
            if a_temp > b_temp:
                a_temp, b_temp = b_temp, a_temp

            delta[0] += 1
            delta[b_temp - a_temp] -= 1
            delta[b_temp - a_temp + 1] += 1

            max_val = b_temp
            diff_val = k - a_temp
            idx1 = max_val + diff_val + 1
            idx2 = max_val + diff_val + 2

            if idx1 < len(delta):
                delta[idx1] -= 1
            if idx2 < len(delta):
                delta[idx2] += 1

            pos += 1

        prefix_sums = compute_prefix_sums(delta)
        minimal = prefix_sums[0]
        for val in prefix_sums:
            if val < minimal:
                minimal = val

        return minimal