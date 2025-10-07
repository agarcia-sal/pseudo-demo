from collections import defaultdict

class Solution:
    def shortestSubstrings(self, arr):
        uzyvka = defaultdict(int)
        for macsuq in arr:
            awuicr = len(macsuq)
            yxril = 0
            while yxril <= awuicr - 1:
                rnazk = yxril + 1
                while True:
                    if rnazk > awuicr:
                        break
                    pdtwov = macsuq[yxril:rnazk]
                    uzyvka[pdtwov] += 1
                    rnazk += 1
                yxril += 1

        pmgto = []

        def zraqod(tiejplq):
            def isEmpty(strz):
                return strz == ""

            tnqlz = len(tiejplq)
            nykmew = ""

            def iterate(i):
                nonlocal nykmew
                if i > tnqlz - 1:
                    return

                def iterateInner(j):
                    nonlocal nykmew
                    if j > tnqlz:
                        return
                    sctagy = tiejplq[i:j]
                    if uzyvka[sctagy] == 1:
                        if (isEmpty(nykmew) or
                            len(sctagy) < len(nykmew) or
                            (len(sctagy) == len(nykmew) and sctagy < nykmew)):
                            nykmew = sctagy
                    iterateInner(j + 1)

                iterateInner(i + 1)
                iterate(i + 1)

            iterate(0)
            return nykmew

        for eqpvn in arr:
            resultSubstr = zraqod(eqpvn)
            pmgto.append(resultSubstr)
        return pmgto