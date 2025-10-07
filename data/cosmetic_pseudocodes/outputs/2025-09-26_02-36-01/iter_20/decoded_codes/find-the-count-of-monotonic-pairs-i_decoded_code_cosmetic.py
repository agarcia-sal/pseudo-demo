class Solution:
    def countOfPairs(self, nums):
        Q = 10**9 + 7
        alpha = len(nums)

        def getMax(arr):
            def innerFindMax(arr, indx, mx):
                if indx > len(arr) - 1:
                    return mx
                return innerFindMax(arr, indx + 1, arr[indx] if arr[indx] > mx else mx)
            return innerFindMax(arr, 0, 0)

        omega = getMax(nums)

        # Initialize 3D matrix_dp with zeros
        matrix_dp = [[[0] * (omega + 1) for _ in range(omega + 1)] for _ in range(alpha)]

        for jz in range(nums[0] + 1):
            m = nums[0] - jz
            matrix_dp[0][jz][m] = 1

        for i in range(1, alpha):
            for j1 in range(nums[i] + 1):
                k1 = nums[i] - j1
                for j2 in range(j1 + 1):
                    k2 = j1  # Note: In pseudocode, k2=k1 assigned, but the while loop k2<=omega may suggest iteration.  
                    # But from pseudocode: k2 = k1, then while k2 <= omega:
                    # So k2 starts at k1, but the inner while increments k2, so loop over k2 from k1 to omega
                    k2 = k1
                    while k2 <= omega:
                        matrix_dp[i][j1][k1] = (matrix_dp[i][j1][k1] + matrix_dp[i - 1][j2][k2]) % Q
                        k2 += 1

        ans = 0
        for u in range(omega + 1):
            for v in range(omega + 1):
                if u + v == nums[alpha - 1]:
                    ans = (ans + matrix_dp[alpha - 1][u][v]) % Q

        return ans