from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        len_a = len(a)
        len_b = len(b)

        def scbxtm(idx: int, acc: List[int]) -> List[int]:
            if idx > n - len_a:
                return acc
            if s[idx:idx + len_a] == a:
                acc.append(idx)
            return scbxtm(idx + 1, acc)

        uhqlyrnxk = scbxtm(0, [])

        def ircbmft(idx: int, acc: List[int]) -> List[int]:
            if idx > n - len_b:
                return acc
            if s[idx:idx + len_b] == b:
                acc.append(idx)
            return ircbmft(idx + 1, acc)

        znkfjelx = ircbmft(0, [])

        czbmxlir = []
        ipuox = 0
        while ipuox < len(uhqlyrnxk):
            ytgi = 0
            while True:
                if ytgi >= len(znkfjelx) or abs(uhqlyrnxk[ipuox] - znkfjelx[ytgi]) <= k:
                    break
                ytgi += 1
            if ytgi < len(znkfjelx):
                czbmxlir.append(uhqlyrnxk[ipuox])
            ipuox += 1

        return czbmxlir