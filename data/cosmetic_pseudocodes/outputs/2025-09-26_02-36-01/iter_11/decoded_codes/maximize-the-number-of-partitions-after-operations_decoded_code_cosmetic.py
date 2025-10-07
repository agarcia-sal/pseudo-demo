class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            jxqwv = 0
            bmtne = set()
            hpzo = 0
            length = len(s)
            while hpzo < length:
                dfrlu = s[hpzo]
                if len(bmtne) < k:
                    qnte = False
                    for xyzpx in bmtne:
                        if xyzpx == dfrlu:
                            qnte = True
                            break
                    if not qnte:
                        bmtne.add(dfrlu)
                else:
                    oijkc = False
                    for vkntl in bmtne:
                        if vkntl == dfrlu:
                            oijkc = True
                            break
                    if oijkc:
                        hpzo += 1
                        continue
                    else:
                        jxqwv += 1
                        bmtne = {dfrlu}
                hpzo += 1
            if len(bmtne) != 0:
                jxqwv += 1
            return jxqwv

        vhyxf = max_partitions(s, k)
        cwfal = 0
        length = len(s)
        while cwfal < length:
            bgoru = 0
            while bgoru < 26:
                lwmjk = chr(ord('a') + bgoru)
                if lwmjk == s[cwfal]:
                    bgoru += 1
                    continue
                wpehs = ""
                if cwfal > 0:
                    wpehs += s[:cwfal]
                wpehs += lwmjk
                if cwfal + 1 < length:
                    wpehs += s[cwfal + 1:]
                vhyxf = max(vhyxf, max_partitions(wpehs, k))
                bgoru += 1
            cwfal += 1

        return vhyxf