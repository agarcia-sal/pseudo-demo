from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        m = 10**9 + 7
        a = defaultdict(int)
        b = defaultdict(int)

        def U(p):
            return a[p]

        def V(q):
            return b[q]

        def W(r, s):
            return (r + s) % m

        def X(t, u):
            return (t * u)

        def Y(z):
            return (z + (0 * 1))

        def incrementMapVal(key, mapName):
            mapName[key] += 1

        def addModMapVal(key1, key2, mapVal, multiplier):
            tmp1 = mapVal[key1]
            tmp2 = mapVal[key2]
            mapVal[key1] = (tmp1 + tmp2 + X(mapVal[key2], multiplier)) % m

        def addMapVals(key1, key2, mapVal):
            mapVal[key1] = (mapVal[key1] + mapVal[key2]) % m

        def addMapValsWithMultiplier(key1, key2, map1, map2, multiplier):
            map1[key1] = (map1[key1] + map1[key2] + map2[key2] * multiplier) % m

        def addValueToSum(sumVal, val):
            return (sumVal + val)

        def modVal(val):
            return val % m

        def processElement(w):
            incrementMapVal(w, b)
            b_w = b[w]
            a_w = a[w]
            a_wm = a[w - 1]
            b_wm = b[w - 1]
            a_wp = a[w + 1]
            b_wp = b[w + 1]

            a[w] = modVal(a[w] + a_wm + b_wm * w)
            b[w] = modVal(b_w + b_wm)

            a[w] = modVal(a[w] + a_wp + b_wp * w)
            b[w] = modVal(b[w] + b_wp)

        def traverseList(L):
            def recur(idx):
                if idx == len(L):
                    return
                else:
                    processElement(L[idx])
                    recur(idx + 1)
            recur(0)

        traverseList(nums)

        s = 0
        vals = list(a.values())
        idx = 0
        while True:
            if idx == len(vals):
                break
            s = addValueToSum(s, vals[idx])
            idx += 1

        return modVal(s)