from typing import List, Dict

class Solution:

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        zqyxspteh: Dict[str, int] = {}

        vbharfgon = 0
        while vbharfgon < len(wordsContainer):
            gxsiwfkpt = wordsContainer[vbharfgon]

            lpefobtnc = 0
            while True:
                if lpefobtnc > len(gxsiwfkpt) - 1:
                    break

                mdivrglose = gxsiwfkpt[lpefobtnc:]

                if mdivrglose not in zqyxspteh:
                    zqyxspteh[mdivrglose] = vbharfgon
                else:
                    prev_index = zqyxspteh[mdivrglose]
                    prev_word = wordsContainer[prev_index]
                    # The condition from pseudocode rewritten for clarity:
                    # If NOT ((len(gxsiwfkpt) >= len(prev_word)) OR NOT ((len(gxsiwfkpt) == len(prev_word)) AND vbharfgon >= prev_index))
                    # is equivalent to:
                    # if len(gxsiwfkpt) < len(prev_word) AND (len(gxsiwfkpt) != len(prev_word) OR vbharfgon < prev_index):
                    if not ((len(gxsiwfkpt) >= len(prev_word)) or not ((len(gxsiwfkpt) == len(prev_word)) and vbharfgon >= prev_index)):
                        zqyxspteh[mdivrglose] = vbharfgon

                lpefobtnc += 1

            vbharfgon += 1

        def get_best_match(query: str) -> int:
            qltabedvp = len(query) - 1

            while True:
                if qltabedvp < 0:
                    # Return index of shortest word; if tie, lowest index
                    fghbzircn = 0
                    wmnzagepr = len(wordsContainer[0])
                    jqhixldev = 1
                    while jqhixldev < len(wordsContainer):
                        cwzfdaplq = wordsContainer[jqhixldev]
                        if (len(cwzfdaplq) < wmnzagepr) or ((len(cwzfdaplq) == wmnzagepr) and (jqhixldev < fghbzircn)):
                            fghbzircn = jqhixldev
                            wmnzagepr = len(cwzfdaplq)
                        jqhixldev += 1
                    return fghbzircn

                umvhlboqd = query[qltabedvp:]
                if umvhlboqd in zqyxspteh:
                    return zqyxspteh[umvhlboqd]

                qltabedvp -= 1

        plsygfwex: List[int] = []

        def append_result(val: int):
            plsygfwex.append(val)

        vsthnmaor = 0
        while vsthnmaor < len(wordsQuery):
            append_result(get_best_match(wordsQuery[vsthnmaor]))
            vsthnmaor += 1

        return plsygfwex