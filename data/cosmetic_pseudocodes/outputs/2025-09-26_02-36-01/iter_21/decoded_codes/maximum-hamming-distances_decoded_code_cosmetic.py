class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:
        def calculateDifference(a: str, b: str) -> int:
            c = 0
            d = 0
            while d < len(a):
                if a[d] != b[d]:
                    c += 1
                d += 1
            return c

        def convertToBinary(value: int) -> str:
            f = ""
            g = value
            while len(f) < m:
                h = chr((g % 2) + 48)
                f = h + f
                g //= 2
            return f

        e = []
        i = 0
        while i < len(nums):
            e.append(convertToBinary(nums[i]))
            i += 1

        j = []
        k = 0
        while k < len(nums):
            m_var = 0
            l = 0
            while l < len(nums):
                if k != l:
                    n = calculateDifference(e[k], e[l])
                    if n > m_var:
                        m_var = n
                l += 1
            j.append(m_var)
            k += 1

        return j