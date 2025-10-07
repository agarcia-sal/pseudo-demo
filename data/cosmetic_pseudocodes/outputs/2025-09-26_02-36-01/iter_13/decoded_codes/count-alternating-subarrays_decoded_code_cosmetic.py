class Solution:
    def countAlternatingSubarrays(self, nums):
        length_var = len(nums)
        if length_var == 0:
            return 0

        def calc_length(arr):
            res = 0
            cur_len = 0

            def recurse(k):
                nonlocal res, cur_len
                if k >= length_var:
                    return
                if k == 0:
                    cur_len = 1
                    res += 1
                else:
                    if arr[k] != arr[k - 1]:
                        cur_len += 1
                    else:
                        cur_len = 1
                    res += (cur_len - 1)
                # Update the outer cur_len variable
                nonlocal cur_len
                recurse(k + 1)

            recurse(0)
            return res

        return calc_length(nums)