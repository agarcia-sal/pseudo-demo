class Solution:
    def betterCompression(self, compressed: str) -> str:
        def incrementMapValue(map_, key, delta):
            if key not in map_:
                map_[key] = 0
            map_[key] += delta

        u1 = ""
        u2 = 0
        m1 = {}
        i1 = 0

        while i1 < len(compressed):
            c1 = compressed[i1]
            if ('a' <= c1 <= 'z') or ('A' <= c1 <= 'Z'):
                if u1 != "":
                    incrementMapValue(m1, u1, u2)
                u1 = c1
                u2 = 0
            else:
                # c1 is digit character, convert to int and update u2 as per base 10 accumulation
                u2 = u2 * 10 + (ord(c1) - ord('0'))
            i1 += 1

        if u1 != "":
            incrementMapValue(m1, u1, u2)

        def sortKeys(d):
            keysList = list(d.keys())

            def quickSort(arr):
                if len(arr) <= 1:
                    return arr
                pivot = arr[0]
                less = []
                more = []
                for i in range(1, len(arr)):
                    if arr[i] < pivot:
                        less.append(arr[i])
                    else:
                        more.append(arr[i])
                return quickSort(less) + [pivot] + quickSort(more)

            return quickSort(keysList)

        sKeys = sortKeys(m1)

        def toString(num):
            if num == 0:
                return "0"
            r = ""
            n = num

            def digitChar(d):
                zeroAscii = 48
                code = zeroAscii + d
                return chr(code)

            while n > 0:
                d = n - (n // 10) * 10
                r = digitChar(d) + r
                n = n // 10
            return r

        l2 = []
        for ch in sKeys:
            part = ch + toString(m1[ch])
            l2.append(part)

        r2 = ""
        j = 0
        while True:
            if j >= len(l2):
                break
            r2 += l2[j]
            j += 1

        return r2