from typing import List


def anti_shuffle(input_string: str) -> str:
    def λζμ𝛼𝚢𝛀𝛊𝓁𝔷𝓔ζ(𝔟𝗤: List[str]) -> List[str]:
        if not 𝔟𝗤:
            return []
        ᚠᛟ = 𝔟𝗤[0]

        def 𝕻𝖋(s: str, r𝕎: List[str]) -> str:
            if not r𝕎:
                return s
            first = r𝕎[0]
            # Append in order: max(s, first) + min(s, first), then recurse with rest of list
            return 𝕻𝖋(
                (s if s >= first else first) + (first if s >= first else s),
                r𝕎[1:],
            )

        𝕻𝖋_result = 𝕻𝖋("", list(ᚠᛟ))
        return [𝕻𝖋_result] + λζμ𝛼𝚢𝛀𝛊𝓁𝔷𝓔ζ(𝔟𝗤[1:])

    Ϝ䷁𝟙𝗓𝗊𝟢𝗅𝗐𝗙 = input_string.split()
    𝙣𝙎𝙩𝙃𝟭𝗔𝗋𝗐𝗙𝗄𝗰: List[str] = []

    def ƗƐƐƖƐɆɛˁ(
        f𝞅: List[str], e𝙓𝞨𝙢: List[str], 𝟂𝓋: int
    ) -> List[str]:
        if not e𝙓𝞨𝙢:
            return f𝞅
        𝛗𝗇𝗉𝟬 = λζμ𝛼𝚢𝛀𝛊𝓁𝔷𝓔ζ([e𝙓𝞨𝙢[0]])[0]
        𝞅 = f𝞅 + [𝛗𝗇𝗉𝟬]
        return ƗƐƐƖƐɆɛˁ(𝞅, e𝙓𝞨𝙢[1:], 𝟂𝓋)

    𝙣𝙎𝙩𝙃𝟭𝗔𝗋𝗐𝗙𝗄𝗈 = ƗƐƐƖƐɆɛˁ([], Ϝ䷁𝟙𝗓𝗊𝟢𝗅𝗐𝗙, 0)
    return " ".join(𝙣𝙎𝙩𝙃𝟭𝗔𝗋𝗐𝗙𝗄𝗈)