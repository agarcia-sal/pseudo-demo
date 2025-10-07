class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        m = len(nums)
        y = 10**9 + 1  # representing infinity

        z = 0
        while True:
            if z > m - 1:
                break

            aa = 0
            bb = z
            while bb <= m - 1:
                aa |= nums[bb]

                cc = k - aa
                dd = -cc if cc < 0 else cc

                if dd < y:
                    y = dd

                if dd == 0:
                    return 0

                bb += 1
            z += 1

        return y