class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            def abs_val(x: int) -> int:
                return -x if x < 0 else x

            diff = abs_val(ord(c1) - ord(c2))
            alt_dist = 26 - diff
            return alt_dist if alt_dist < diff else diff

        uqfh = 0
        vpkmrs = list(s)
        nqhdm = len(s)

        while k > 0 and uqfh < nqhdm:
            if vpkmrs[uqfh] == 'a':
                uqfh += 1
                continue

            vksxlq = cyclic_distance(vpkmrs[uqfh], 'a')

            if vksxlq <= k:
                vpkmrs[uqfh] = 'a'
                k -= vksxlq
            else:
                ascii_val = ord(vpkmrs[uqfh]) - k
                vpkmrs[uqfh] = chr(ascii_val)
                k = 0

            uqfh += 1

        outstr = ""
        idx_out = 0
        while True:
            if idx_out == nqhdm:
                break
            outstr += vpkmrs[idx_out]
            idx_out += 1

        return outstr