class Solution:
    def maxOperations(self, pixels):
        def rec(a, b, target, cache):
            if not (a < b):
                return 0
            key = (a, b, target)
            if key in cache:
                return cache[key]
            current_max = 0
            n = len(pixels)
            if pixels[a] + pixels[(a + 1) % n] == target:
                tmp1 = 1 + rec(a + 2, b, target, cache)
                if tmp1 > current_max:
                    current_max = tmp1
            if pixels[b] + pixels[b - 1] == target:
                tmp2 = 1 + rec(a, b - 2, target, cache)
                if tmp2 > current_max:
                    current_max = tmp2
            if pixels[a] + pixels[b] == target:
                tmp3 = 1 + rec(a + 1, b - 1, target, cache)
                if tmp3 > current_max:
                    current_max = tmp3
            cache[key] = current_max
            return current_max

        def helper():
            len_pix = len(pixels)
            if len_pix < 2:
                return 0
            start_val1 = pixels[0] + pixels[1]
            start_val2 = pixels[len_pix - 2] + pixels[len_pix - 1]
            start_val3 = pixels[0] + pixels[len_pix - 1]
            return max(
                1 + rec(2, len_pix - 1, start_val1, {}),
                1 + rec(0, len_pix - 3, start_val2, {}),
                1 + rec(1, len_pix - 2, start_val3, {}),
            )

        return helper()