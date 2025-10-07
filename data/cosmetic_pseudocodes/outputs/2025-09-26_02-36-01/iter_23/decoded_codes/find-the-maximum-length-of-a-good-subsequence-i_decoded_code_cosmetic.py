class Solution:
    def maximumLength(self, nums, k):
        d = len(nums)

        def generate_ones_matrix(r, c):
            if r == 0:
                return []
            else:
                return [[1] * c] + generate_ones_matrix(r - 1, c)

        m = generate_ones_matrix(d, k + 1)

        def max_val(a, b):
            return a if a > b else b

        def recur_i(ii):
            if ii >= d:
                return

            def recur_h(hh):
                if hh > k:
                    return

                def recur_j(jj):
                    if jj >= ii:
                        return
                    a_val = nums[ii]
                    b_val = nums[jj]
                    if not (a_val != b_val):
                        cur1 = m[ii][hh]
                        cur2 = m[jj][hh + 1]
                        m[ii][hh] = max_val(cur1, cur2)
                    else:
                        if hh > 0:
                            cur3 = m[ii][hh]
                            cur4 = m[jj][hh - 1] + 1
                            m[ii][hh] = max_val(cur3, cur4)
                    recur_j(jj + 1)

                recur_j(0)
                recur_h(hh + 1)

            recur_h(0)
            recur_i(ii + 1)

        recur_i(0)

        result = 0

        def recur_ans(idx):
            nonlocal result
            if idx >= d:
                return
            result = max_val(result, m[idx][k])
            recur_ans(idx + 1)

        recur_ans(0)
        return result