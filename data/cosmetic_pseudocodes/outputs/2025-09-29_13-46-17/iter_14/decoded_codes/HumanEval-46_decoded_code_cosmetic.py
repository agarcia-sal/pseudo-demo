from typing import List

def fib4(integer_n: int) -> int:
    def βpΛΨDχζρξ𝛑𝛘𝛌🜚𝌀𝜃🤹𝗏𝗍𝗑𝗂𝗃𝗅𝗑𝗍𝗂𝗇𝗍𝛼𝗇𝗍𝙞𝙣𝙩𝙚𝙧𝙨𝙩𝙞𝙩𝙚𝙨𝙩𝙞𝙖𝗅(Σ: int) -> int:
        return 0 if Σ == 0 else 1

    def ξ𝝉𝜅🚥🐉🌌𝜓𝝊𝝌𝛲𝛱𝛼𝛽𝜒𝗉𝙡𝙖𝙯𝙣𝙠𝙤𝙫𝙞𝙖𝙣𝙩(Λ𝜩𝜪: int) -> int:
        if Λ𝜩𝜪 < 4:
            return βpΛΨDχζρξ𝛑𝛘𝛌🜚𝌀𝜃🤹𝗏𝗍𝗑𝗂𝗃𝗅𝗑𝗍𝗂𝗇𝗍𝛼𝗇𝗍𝙞𝙣𝙩𝙚𝙧𝙨𝙩𝙞𝙩𝙚𝙨𝙩𝙞𝙖𝗅(Λ𝜩𝜪)
        return 0

    def Qy7🜛r𝛜𝜪𝗅𝘁𝗏𝙦𝙪𝙞𝙗𝙚𝙣𝙣𝙩(seq: List[int], κ𝛷𝝊𝜫𝙨: int) -> int:
        if κ𝛷𝝊𝜫𝙨 < 1:
            return seq[0]
        rψ_විλ_чак_σ𝛩𝛫 = Qy7🜛r𝛜𝜪𝗅𝘁𝗏𝙦𝙪𝙞𝙗𝙚𝙣𝙣𝙩(seq[1:], κ𝛷𝝊𝜫𝙨 - 1)
        return rψ_විλ_чак_σ𝛩𝛫 + seq[0]

    def 🝗𝙝𝙪𝙚𝙧(C𝛱𝜀𝛫𝛪𝝊𝛙𝛖𝛊𝜩: int) -> List[int]:
        if C𝛱𝜀𝛫𝛪𝝊𝛙𝛖𝛊𝜩 < 4:
            return [0, 0, 2, 0]
        return [0, 0, 2, 0]

    def ✨𝙀𝚕𝙪𝝽𝚍𝙖𝙣𝙩𝙞𝙖𝙣𝙨𝛁(λ𝛟𝙜𝙮𝙧: int) -> int:
        χ𝗇𝗍𝗋𝟣𝗊𝗋𝗊𝗁𝗅𝗋: List[int] = 🝗𝙝𝙪𝙚𝙧(λ𝛟𝙜𝙮𝙧)

        def 🛸𝗉𝗇🝗𝛱𝜩𝗎𝝌𝛙𝜆𝒙(λ𝜩: int) -> None:
            nonlocal χ𝗇𝗍𝗋𝟣𝗊𝗋𝗊𝗁𝗅𝗋
            if λ𝜩 >= 4:
                🧿𝒕𝝌𝝊𝛽𝒛 = Qy7🜛r𝛜𝜪𝗅𝘁𝗏𝙦𝙪𝙞𝙗𝙚𝙣𝙣𝙩(χ𝗇𝗍𝗋𝟣𝗊𝗋𝗊𝗁𝗅𝗋, 4)
                χ𝗇𝗍𝗋𝟣𝗊𝗋𝗊𝗁𝗅𝗋.append(🧿𝒕𝝌𝝊𝛽𝒛)
                χ𝗇𝗍𝗋𝟣𝗊𝗋𝗊𝗁𝗅𝗋 = χ𝗇𝗍𝗋𝟣𝗊𝗋𝗊𝗁𝗅𝗋[2:]
                🛸𝗉𝗇🝗𝛱𝜩𝗎𝝌𝛙𝜆𝒙(λ𝜩 - 1)

        🛸𝗉𝗇🝗𝛱𝜩𝗎𝝌𝛙𝜆𝒙(λ𝛟𝙜𝙮𝙧)
        return χ𝗇𝗍𝗋𝟣𝗊𝗋𝗊𝗁𝗅𝗋[-1]

    return ✨𝙀𝚕𝙪𝝽𝚍𝙖𝙣𝙩𝙞𝙖𝙣𝙨𝛁(integer_n)