from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        def inplaceSort(arr):
            u = 1
            while u < len(arr):
                v = u
                while v > 0 and arr[v - 1] > arr[v]:
                    arr[v], arr[v - 1] = arr[v - 1], arr[v]
                    v -= 1
                u += 1

        inplaceSort(nums)

        b25 = 0
        t1u = defaultdict(int)

        n3r = 0
        while n3r < len(nums):
            zqf = set()
            zqf.add(nums[n3r])

            ksr = str(nums[n3r])
            l87 = list(ksr)
            v04 = len(l87)

            yx9 = 0
            while yx9 < v04:
                ekc = 0
                while ekc < yx9:
                    l87[ekc], l87[yx9] = l87[yx9], l87[ekc]

                    vo2 = "".join(l87)
                    zqf.add(int(vo2))

                    m1z = ekc + 1
                    while m1z < v04:
                        wl0 = ekc + 1
                        while wl0 < m1z:
                            l87[wl0], l87[m1z] = l87[m1z], l87[wl0]

                            rbi = "".join(l87)
                            zqf.add(int(rbi))

                            l87[wl0], l87[m1z] = l87[m1z], l87[wl0]
                            wl0 += 1
                        m1z += 1

                    l87[ekc], l87[yx9] = l87[yx9], l87[ekc]
                    ekc += 1
                yx9 += 1

            for xd8 in zqf:
                b25 += t1u[xd8]

            t1u[nums[n3r]] += 1

            n3r += 1

        return b25