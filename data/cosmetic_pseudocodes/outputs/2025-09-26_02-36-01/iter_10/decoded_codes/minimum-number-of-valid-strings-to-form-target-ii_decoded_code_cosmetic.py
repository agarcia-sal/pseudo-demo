class Solution:
    def minValidStrings(self, words, target):
        def extractPrefixes(arr):
            K0 = set()
            for Sx in arr:
                wI = 1
                while wI <= len(Sx):
                    uN = Sx[:wI]
                    K0.add(uN)
                    wI += 1
            return K0

        MUST = extractPrefixes(words)

        L_ = len(target)
        dpArray = [float('inf')] * (L_ + 1)
        dpArray[0] = 0

        for x_ in range(1, L_ + 1):
            y_ = x_
            while y_ > 0:
                TK = target[y_ - 1:x_]
                if TK in MUST:
                    pQ = dpArray[y_ - 1] + 1
                    if pQ < dpArray[x_]:
                        dpArray[x_] = pQ
                y_ -= 1

        return dpArray[L_] if dpArray[L_] != float('inf') else -1