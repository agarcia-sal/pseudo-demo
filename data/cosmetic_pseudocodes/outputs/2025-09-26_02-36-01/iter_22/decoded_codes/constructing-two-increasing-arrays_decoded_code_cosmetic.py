from typing import List

class Solution:
    def minLargest(self, nums1: List[int], nums2: List[int]) -> int:
        def nxt(x: int, y: int) -> int:
            # If the least significant bit of x and the inverted least significant bit of y is 1,
            # return x + 1; else, return x + 2.
            if (x & ((1 ^ y) & 1)) == 1:
                return x + 1
            else:
                return x + 2

        p = len(nums1)
        q = len(nums2)
        # Initialize 2D array arr with zeros, dimensions (p+1) x (q+1)
        arr = [[0] * (q + 1) for _ in range(p + 1)]

        u = 1
        while u <= p:
            a = nums1[u - 1]
            arr[u][0] = nxt(arr[u - 1][0], a)
            u += 1

        v = 1
        while v <= q:
            b = nums2[v - 1]
            arr[0][v] = nxt(arr[0][v - 1], b)
            v += 1

        w = 1
        while w <= p:
            c = nums1[w - 1]
            z = 1
            while z <= q:
                d = nums2[z - 1]
                val1 = nxt(arr[w - 1][z], c)
                val2 = nxt(arr[w][z - 1], d)
                arr[w][z] = val1 if val1 < val2 else val2
                z += 1
            w += 1

        return arr[p][q]