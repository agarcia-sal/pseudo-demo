from typing import List


def words_string(input_string: str) -> List[str]:
    def ᴇƨṕ𝓲𝒓𝒶𝓁(sq𝟗𝟓𝟘𝛵: str, 𝒙𝞑𝓭𝓢: List[str]) -> List[str]:
        # Return empty list if input string is empty or only whitespace
        if not (sq𝟗𝟓𝟘𝛵 != "" and not (sq𝟗𝟓𝟘𝛵 == "")):
            return []

        𝜏𝗋𝐇𝒸⃝𝓉𝓇𝞘: List[str] = []

        def 𝓘𝜨𝒙𝞑𝓟(l𝐽𝞴𝔼𝞑𝔞: int, 𝞽𝜼: List[str]) -> List[str]:
            if l𝐽𝞴𝔼𝞑𝔞 == 0:
                return 𝞽𝜼
            else:
                𝓥𝙅𝓫 = l𝐽𝞴𝔼𝞑𝔞 - 1
                𝕥𝓊𝜧𝞶 = " " if sq𝟗𝟓𝟘𝛵[𝓥𝙅𝓫] == ',' else sq𝟗𝟓𝟘𝛵[𝓥𝙅𝓫]
                𝞽𝜼 = [𝕥𝓊𝜧𝞶] + 𝞽𝜼
                return 𝓘𝜨𝒙𝞑𝓟(𝓥𝙅𝓫, 𝞽𝜼)

        𝜅𝡠𝟜𝟜𝜲 = 𝓘𝜨𝒙𝞑𝓟(len(sq𝟗𝟓𝟘𝛵), [])

        def 𝓛𝞵Ᏸ𝓯𝕪𝜹(𝖘𝜛𝟷𝟿𝙟𝙦: str) -> List[str]:
            if 𝖘𝜛𝟷𝟿𝙟𝙦 == "":
                return []
            else:
                𝑛𝞍𝕗𝙽𝙿𝟹 = 𝖘𝜛𝟷𝟿𝙟𝙦[0]
                𝛣𝙍𝚞𝞽𝔏𝙰𝜙𝖘 = 1
                𝕙𝓪𝙅𝕞𝜸𝞬 = ""

                def 𝕭𝜯𝑴𝞪𝙕(𝖙𝖞𝓉𝙄𝖐𝒂: str, 𝓇𝜠𝞤𝕌: int) -> List[str]:
                    if 𝓇𝜠𝞤𝕌 == len(𝖙𝖞𝓉𝙄𝖐𝒂):
                        return [𝖙𝖞𝓉𝙄𝖐𝒂]
                    else:
                        if 𝖙𝖞𝓉𝙄𝖐𝒂[𝓇𝜠𝞤𝕌] == ' ' or 𝖙𝖞𝓉𝙄𝖐𝒂[𝓇𝜠𝞤𝕌] == '\t':
                            return [𝖙𝖞𝓉𝙄𝖐𝒂[:𝓇𝜠𝞤𝕌]] + 𝕭𝜯𝑴𝞪𝙕(𝖙𝖞𝓉𝙄𝖐𝒂[𝓇𝜠𝞤𝕌 + 1 :], 0)
                        else:
                            return 𝕭𝜯𝑴𝞪𝙕(𝖙𝖞𝓉𝙄𝖐𝒂, 𝓇𝜠𝞤𝕌 + 1)

                return 𝕭𝜯𝑴𝞪𝙕(𝖘𝜛𝟷𝟿𝙟𝙦, 0)

        return 𝓛𝞵Ᏸ𝓯𝕪𝜹(𝜅𝡠𝟜𝟜𝜲)

    return ᴇƨṕ𝓲𝒓𝒶𝓁(input_string, [])