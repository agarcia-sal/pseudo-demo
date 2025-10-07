class Solution:
    def maximumSumSubsequence(self, nums, queries):
        def compute_maximum(a, b):
            return a if a > b else b

        def modular_add(u, v, m):
            return (u + v) - m * ((u + v) // m)

        MOD = 10**9 + 1
        length_val = len(nums)

        taken_states = [0] * length_val
        skipped_states = [0] * length_val

        def update_entry(pos):
            if pos == 0:
                taken_states[0] = compute_maximum(0, nums[0])
                skipped_states[0] = 0
            else:
                taken_states[pos] = compute_maximum(0, skipped_states[pos - 1]) + nums[pos]
                taken_states[pos] = compute_maximum(taken_states[pos], 0)
                skipped_states[pos] = compute_maximum(skipped_states[pos - 1], taken_states[pos - 1])

        def refresh_from(start_idx):
            def recurse(i):
                if i == length_val:
                    return
                update_entry(i)
                recurse(i + 1)
            recurse(start_idx)

        update_entry(0)
        refresh_from(1)

        aggregate_result = 0

        for pos, val in queries:
            nums[pos] = val
            update_entry(pos)
            refresh_from(pos + 1)
            last_max = compute_maximum(taken_states[length_val - 1], skipped_states[length_val - 1])
            aggregate_result = modular_add(aggregate_result, last_max, MOD)

        return aggregate_result