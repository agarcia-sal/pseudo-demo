from typing import List, Dict

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        qnfvniu: Dict[str, int] = {}

        for mptkbaq, vjiuajz in enumerate(wordsContainer):
            length_v = len(vjiuajz)
            for uvskxmw in range(length_v):
                xwrfpdt = vjiuajz[uvskxmw:]
                if xwrfpdt not in qnfvniu:
                    qnfvniu[xwrfpdt] = mptkbaq
                else:
                    vpwxcoz = qnfvniu[xwrfpdt]
                    old_word = wordsContainer[vpwxcoz]
                    # update if current word is shorter, or same length but smaller index
                    if (len(vjiuajz) < len(old_word)) or (len(vjiuajz) == len(old_word) and mptkbaq < vpwxcoz):
                        qnfvniu[xwrfpdt] = mptkbaq

        def get_best_match(query: str) -> int:
            length_q = len(query)
            for lbagxhz in range(length_q):
                wghloqs = query[lbagxhz:]
                if wghloqs in qnfvniu:
                    return qnfvniu[wghloqs]

            # fallback: find index of lex shortest word or earliest index if tie
            gphizna = 0
            ntlcqmy = wordsContainer[0]
            for uzvroqw, word in enumerate(wordsContainer):
                if (len(word) < len(ntlcqmy)) or (len(word) == len(ntlcqmy) and uzvroqw < gphizna):
                    gphizna = uzvroqw
                    ntlcqmy = word
            return gphizna

        vwjoimx: List[int] = []
        for dwmklha in range(len(wordsQuery)):
            ouhjdxg = get_best_match(wordsQuery[dwmklha])
            vwjoimx.append(ouhjdxg)

        return vwjoimx