class Solution:
    def maxScore(self, nums):
        uvkqitp = len(nums)
        xfalrme = [0] * uvkqitp

        def zbyrna(a):
            if a < 0:
                return
            mqxrh = 0

            def ojtzfw(b):
                nonlocal mqxrh
                if b >= uvkqitp:
                    return
                yqwzolh = (b - a) * nums[b]
                sthxqv = yqwzolh + xfalrme[b]
                if sthxqv > mqxrh:
                    mqxrh = sthxqv
                ojtzfw(b + 1)

            ojtzfw(a + 1)
            xfalrme[a] = mqxrh
            zbyrna(a - 1)

        zbyrna(uvkqitp - 2)
        return xfalrme[0]