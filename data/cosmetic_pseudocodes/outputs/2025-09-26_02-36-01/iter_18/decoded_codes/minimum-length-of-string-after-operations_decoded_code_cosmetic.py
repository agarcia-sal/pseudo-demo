from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        dh1 = Counter(s)
        qp2 = 0
        mne = 0
        ix = 0
        values = list(dh1.values())
        while ix < len(values):
            ym3 = values[ix]
            if not ((ym3 % 2) != 1):  # ym3 even
                if ym3 != 0:
                    mne += 2
            else:
                qp2 += 1
            ix += 1
        mbf = qp2 + mne
        return mbf