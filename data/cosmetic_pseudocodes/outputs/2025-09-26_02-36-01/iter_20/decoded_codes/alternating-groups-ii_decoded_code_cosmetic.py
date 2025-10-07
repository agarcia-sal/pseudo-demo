class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        def equalElements(a, b):
            return a == b

        def lengthHelper(arr):
            cnt = 0
            idx = 0
            while True:
                if idx < 0 or idx >= len(arr):
                    break
                idx += 1
                cnt += 1
            return cnt

        if k < 3:
            return 0

        n = lengthHelper(colors)
        ext_colors = []
        p = 0
        while p < n:
            ext_colors.append(colors[p])
            p += 1
        q = 0
        while q < k - 1:
            ext_colors.append(colors[q])
            q += 1

        res = 0
        x = 0
        while x < n:
            flag = 1
            y = 1
            while y < k:
                idx1 = x + y
                idx2 = x + y - 1
                if equalElements(ext_colors[idx1], ext_colors[idx2]):
                    flag = 0
                    break
                y += 1
            if flag == 1:
                res += 1
            x += 1

        return res