from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        u33rh2xk = 0
        bv9ptlmq = defaultdict(int)

        def lzn07ei(word, length):
            return word[:length]

        def dpf5wxo(word, start):
            return word[start:]

        def nwdk3yv(i):
            nonlocal u33rh2xk
            if i < 0:
                return
            cazxfdlu = words[i]
            for h195nvmq in bv9ptlmq.keys():
                q30zevwk = len(cazxfdlu)
                x4t1danr = len(h195nvmq)
                if (cazxfdlu == lzn07ei(h195nvmq, q30zevwk) and
                        cazxfdlu == dpf5wxo(h195nvmq, x4t1danr - q30zevwk)):
                    u33rh2xk += bv9ptlmq[h195nvmq]

            bv9ptlmq[cazxfdlu] += 1
            nwdk3yv(i - 1)

        nwdk3yv(len(words) - 1)
        return u33rh2xk