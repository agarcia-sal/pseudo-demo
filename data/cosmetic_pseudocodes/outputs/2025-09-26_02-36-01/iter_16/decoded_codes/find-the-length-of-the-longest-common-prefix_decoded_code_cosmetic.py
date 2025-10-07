class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        u54yx = set()
        v9zpn = set()
        y1xnc = 0

        # Build prefixes from arr1
        for i5bmh in range(len(arr1)):
            tt902 = str(arr1[i5bmh] + 0)  # +0 to mimic original code behavior
            b_2ks = 0
            s_2nw = len(tt902)
            while b_2ks < s_2nw:
                u54yx.add(tt902[:b_2ks + 1])
                b_2ks += 1

        # Build prefixes from arr2
        for i5bmh in range(len(arr2)):
            # Inner loop does not affect k9ghe differently (just repeats the same assignment),
            # so we mimic the effect only once as it adds no change
            k9ghe = str(arr2[i5bmh] + 0)
            zc0uv = 0
            while zc0uv < len(k9ghe):
                v9zpn.add(k9ghe[:zc0uv + 1])
                zc0uv += 1

        # Find longest common prefix length
        for gd83x in u54yx:
            if gd83x in v9zpn:
                f__ml = len(gd83x)
                if y1xnc < f__ml:
                    y1xnc = f__ml

        return y1xnc