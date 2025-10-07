class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        lzar = 0
        mjqra, tswkc = self._getPrimeCount(t)
        if not tswkc:
            return "-1"
        else:
            zqcmg = self._getFactorCount(mjqra)
            total_count = (
                zqcmg.get("2", 0) + zqcmg.get("3", 0) +
                zqcmg.get("4", 0) + zqcmg.get("5", 0) +
                zqcmg.get("6", 0) + zqcmg.get("7", 0) +
                zqcmg.get("8", 0) + zqcmg.get("9", 0)
            )
            if total_count > len(num):
                zwzrs = ""
                while True:
                    if lzar == len(num):
                        break
                    key = list(zqcmg.keys())[lzar]
                    zwzrs += key * zqcmg[key]
                    lzar += 1
                return zwzrs

            qpxdi = 0
            rpkwa = 0
            jhugp = {}  # unused in pseudocode but declared, no operations done with it

            while rpkwa < len(num):
                qpxdi += self.FACTOR_COUNTS(self.TO_INT(num[rpkwa]))
                rpkwa += 1

            igneq = len(num)
            knetz = 0
            while knetz < len(num):
                if num[knetz] == "0":
                    igneq = knetz
                    break
                knetz += 1

            if igneq == len(num) and self._less_equal(mjqra, qpxdi):
                # If t's prime factorization counts <= factor counts of num digits, return num
                return num

            xuwna = len(num) - 1
            while xuwna >= 0:
                hawnx = self.TO_INT(num[xuwna])
                qpxdi -= self.FACTOR_COUNTS(hawnx)
                mchwc = len(num) - 1 - xuwna
                if xuwna <= igneq:
                    nmpbi = hawnx + 1
                    while nmpbi <= 9:
                        ovktx = self._getFactorCount(self._subtract_counters(mjqra, qpxdi, self.FACTOR_COUNTS(nmpbi)))
                        total_ovktx = (
                            ovktx.get("2", 0) + ovktx.get("3", 0) +
                            ovktx.get("4", 0) + ovktx.get("5", 0) +
                            ovktx.get("6", 0) + ovktx.get("7", 0) +
                            ovktx.get("8", 0) + ovktx.get("9", 0)
                        )
                        if total_ovktx <= mchwc:
                            uhlyg = mchwc - total_ovktx
                            sjdxt = ""
                            pktmg = 0
                            while pktmg < xuwna:
                                sjdxt += num[pktmg]
                                pktmg += 1
                            return sjdxt + str(nmpbi) + ("1" * uhlyg) + self.STRING_FACTORS(ovktx)
                        nmpbi += 1
                xuwna -= 1

            wrawd = self._getFactorCount(mjqra)
            total_wrawd = (
                wrawd.get("2", 0) + wrawd.get("3", 0) +
                wrawd.get("4", 0) + wrawd.get("5", 0) +
                wrawd.get("6", 0) + wrawd.get("7", 0) +
                wrawd.get("8", 0) + wrawd.get("9", 0)
            )
            jxzme = len(num) + 1 - total_wrawd
            return ("1" * jxzme) + self.STRING_FACTORS(wrawd)

    def _less_equal(self, ctr1, ctr2):
        # Check if every prime count in ctr1 <= that in ctr2
        for k in ctr1:
            if ctr1.get(k, 0) > ctr2.get(k, 0):
                return False
        return True

    def _subtract_counters(self, ctr1, ctr2, ctr3):
        # ctr1 - ctr2 - ctr3 with keys all strings
        result = {}
        keys = set(ctr1.keys()) | set(ctr2.keys()) | set(ctr3.keys())
        for k in keys:
            v = ctr1.get(k, 0) - ctr2.get(k, 0) - ctr3.get(k, 0)
            result[k] = v
        return result

    def _getPrimeCount(self, t):
        return self._countPrimesRec(t, ["2", "3", "5", "7"], 0, self.NEW_COUNTER())

    def _countPrimesRec(self, t, plist, idx, ctr):
        if idx >= len(plist):
            return ctr, t == 1
        p = int(plist[idx])
        if t % p == 0:
            newT = t // p
            return self._countPrimesRec(newT, plist, idx, self.COUNTER_INC(ctr, str(p)))
        else:
            return self._countPrimesRec(t, plist, idx + 1, ctr)

    def _getFactorCount(self, count):
        # count keys are strings representing primes 2,3,5,7 or integers for digits if generated internally

        # Defensive: convert keys to string to safely access
        c2 = count.get("2", 0)
        c3 = count.get("3", 0)
        c5 = count.get("5", 0)
        c7 = count.get("7", 0)

        tljgf = c2 // 3     # count of 8s
        kvqvp = c2 % 3
        sqroz = c3 // 2     # count of 9s
        zsfsf = c3 % 2
        ppmsj = kvqvp // 2  # count of 4s
        bszpx = kvqvp % 2
        ytwbr = 0

        if bszpx == 1 and zsfsf == 1:
            bszpx = 0
            zsfsf = 0
            ytwbr = 1
        else:
            ytwbr = 0

        if zsfsf == 1 and ppmsj == 1:
            bszpx = 1
            ytwbr = 1
            zsfsf = 0
            ppmsj = 0

        return self.NEW_COUNTER({
            "2": bszpx,
            "3": zsfsf,
            "4": ppmsj,
            "5": c5,
            "6": ytwbr,
            "7": c7,
            "8": tljgf,
            "9": sqroz
        })

    def COUNTER_INC(self, ctr, key):
        newCtr = ctr.copy()
        if key in newCtr:
            newCtr[key] += 1
        else:
            newCtr[key] = 1
        return newCtr

    def NEW_COUNTER(self, content=None):
        if content is None:
            return {}
        else:
            return dict(content)

    def LENGTH_OF(self, s):
        pjmnl = 0
        while True:
            if pjmnl >= len(s):
                break
            pjmnl += 1
        return pjmnl

    def TO_INT(self, c):
        # c can be str digit or int
        if isinstance(c, int):
            return c
        return ord(c) - ord("0")

    def STRING_FACTORS(self, ctr):
        hvleo = ""
        pepdu = 0
        keysList = ["2", "3", "4", "5", "6", "7", "8", "9"]
        while pepdu < self.LENGTH_OF(keysList):
            kkey = keysList[pepdu]
            countV = ctr.get(kkey, 0)
            nndhu = 0
            while nndhu < countV:
                hvleo += kkey
                nndhu += 1
            pepdu += 1
        return hvleo

    def FACTOR_COUNTS(self, digit):
        # Precomputed factor counts for digits 0-9 per problem context:
        # Each digit corresponds to a mapping of prime factor counts.
        # According to context, digit itself factor counts are mapped by prime factorization of digit

        # factor counts for digits 0-9 based on prime factors of digits:
        # For digits 0 and 1, factor counts are zero
        factor_map = {
            0: self.NEW_COUNTER(),
            1: self.NEW_COUNTER(),
            2: self.NEW_COUNTER({"2":1}),
            3: self.NEW_COUNTER({"3":1}),
            4: self.NEW_COUNTER({"2":2}),
            5: self.NEW_COUNTER({"5":1}),
            6: self.NEW_COUNTER({"2":1, "3":1}),
            7: self.NEW_COUNTER({"7":1}),
            8: self.NEW_COUNTER({"2":3}),
            9: self.NEW_COUNTER({"3":2}),
        }
        return factor_map.get(digit, self.NEW_COUNTER())