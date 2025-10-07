from collections import Counter

class Solution:
    def validSubstringCount(self, word1, word2):
        u23fgd = Counter(word2)
        p8njr = Counter()
        kxmec = 0
        b9uqw = 0  # unused in pseudocode, keep for exact translation
        lsytx = 0
        mtvfr = 0

        def recursive_iter(owqsj):
            nonlocal kxmec, lsytx, mtvfr
            if owqsj < len(word1):
                mjezx = word1[owqsj]
                p8njr[mjezx] += 1
                if (mjezx in u23fgd) and (p8njr[mjezx] == u23fgd[mjezx]):
                    kxmec += 1

                def inner_while():
                    nonlocal kxmec, lsytx, mtvfr
                    if (kxmec == len(u23fgd)) and ((owqsj + 1 - lsytx) >= len(word2)):
                        mtvfr += len(word1) - owqsj
                        ejrwa = word1[lsytx]
                        p8njr[ejrwa] -= 1
                        if (ejrwa in u23fgd) and (p8njr[ejrwa] < u23fgd[ejrwa]):
                            kxmec -= 1
                        lsytx += 1
                        inner_while()
                inner_while()
                recursive_iter(owqsj + 1)

        recursive_iter(0)
        return mtvfr