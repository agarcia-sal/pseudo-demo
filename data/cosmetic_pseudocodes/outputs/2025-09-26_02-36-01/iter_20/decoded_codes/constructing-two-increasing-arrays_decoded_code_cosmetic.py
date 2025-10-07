class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(a: int, b: int) -> int:
            # If least significant bit of a XOR b is 1, add 1, else add 2
            if ((a & 1) ^ b) == 1:
                r = a + 1
            else:
                r = a + 2
            return r

        U = len(nums1)
        V = len(nums2)

        # Initialize a (U+1) x (V+1) matrix Q filled with zeros
        Q = [[0] * (V + 1) for _ in range(U + 1)]

        # The pseudocode uses 1-based indexing on nums but Python lists are 0-based.
        # So adjust index references by subtracting 1 when accessing nums1 and nums2

        for i in range(1, U + 1):
            z1 = nums1[i - 1]
            p1 = nxt(Q[i - 1][0], z1)
            Q[i][0] = p1

        for j in range(1, V + 1):
            z2 = nums2[j - 1]
            p2 = nxt(Q[0][j - 1], z2)
            Q[0][j] = p2

        for i in range(1, U + 1):
            z1 = nums1[i - 1]
            for j in range(1, V + 1):
                z2 = nums2[j - 1]
                p1 = nxt(Q[i - 1][j], z1)
                p2 = nxt(Q[i][j - 1], z2)
                Q[i][j] = p1 if p1 <= p2 else p2

        return Q[U][V]