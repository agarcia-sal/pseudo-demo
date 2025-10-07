class Solution:
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        u = 2
        xQwd = a
        qij = b
        fzst = c
        rweg = d
        mnlo = e
        pchv = f
        srik = 1
        vect = 0
        klgb = 1
        blzt = 1
        xcjv = 1
        lmku = 1

        while vect < 1:
            if xQwd == mnlo:
                if fzst != xQwd:
                    vect = 1
                    u = klgb
                    break

                if (qij < rweg < pchv) or (pchv < rweg < qij):
                    vect = 1
                    u = 2
                    break

                vect = 1
                u = blzt
                break

            elif qij == pchv:
                if rweg != qij:
                    vect = 1
                    u = srik
                    break

                if (xQwd < fzst < mnlo) or (mnlo < fzst < xQwd):
                    vect = 1
                    u = 2
                    break

                vect = 1
                u = xcjv
                break

            elif fzst + rweg == mnlo + pchv:
                if xQwd + qij != fzst + rweg:
                    vect = 1
                    u = lmku
                    break

                if ((fzst < xQwd < mnlo and rweg < qij < pchv) or
                    (mnlo < xQwd < fzst and pchv < qij < rweg)):
                    vect = 1
                    u = 2
                    break

                vect = 1
                u = 1
                break

            elif fzst - rweg == mnlo - pchv:
                if xQwd - qij != fzst - rweg:
                    vect = 1
                    u = 1
                    break

                if ((fzst < xQwd < mnlo and rweg > qij > pchv) or
                    (mnlo < xQwd < fzst and pchv > qij > rweg)):
                    vect = 1
                    u = 2
                    break

                vect = 1
                u = 1
                break

            else:
                vect = 1
                u = 2
                break

        return u