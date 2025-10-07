class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(a: int, b: int) -> int:
            # If the bitwise AND of a and (1 XOR b) is 1, return a+1, else return a+2
            if (a & (1 ^ b)) == 1:
                return a + 1
            else:
                return a + 2

        length1 = len(nums1)
        length2 = len(nums2)
        # Create dp array of size (length1+1) x (length2+1) initialized with zeros
        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]

        # Fill dp column 0
        for counter1 in range(1, length1 + 1):
            val1 = nums1[counter1 - 1]
            prev_val = dp[counter1 - 1][0]
            dp[counter1][0] = nxt(prev_val, val1)

        # Fill dp row 0
        for counter2 in range(1, length2 + 1):
            val2 = nums2[counter2 - 1]
            prev_val2 = dp[0][counter2 - 1]
            dp[0][counter2] = nxt(prev_val2, val2)

        # Fill the rest of dp
        for i in range(1, length1 + 1):
            val_i = nums1[i - 1]
            for j in range(1, length2 + 1):
                val_j = nums2[j - 1]
                option1 = nxt(dp[i - 1][j], val_i)
                option2 = nxt(dp[i][j - 1], val_j)
                dp[i][j] = option1 if option1 < option2 else option2

        return dp[length1][length2]