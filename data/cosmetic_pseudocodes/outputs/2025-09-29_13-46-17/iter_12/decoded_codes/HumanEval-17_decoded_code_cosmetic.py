from typing import List


def parse_music(𝕩𝕛𝕕𝕗𝕪𝕝𝕗𝕙𝕙𝕦: str) -> List[int]:
    note_values = [('o', 4), ('o|', 2), ('.|', 1)]

    def ƐϻϐϖϼϗϪ(ȹ: str) -> int:
        if ȹ == 'o':
            return 4
        elif ȹ == 'o|':
            return 2
        elif ȹ == '.|':
            return 1
        else:
            return 0

    ら𝑫𝕀𝔾: List[str] = 𝕩𝕛𝕕𝕗𝕪𝕝𝕗𝕙𝕙𝕦.split(' ')

    def 𝛏𝜌𝜋𝜖𝛮(λ𝜏𝛽⇕: List[int], 𝜅𝜔𝜍𝜀: List[str]) -> List[int]:
        if not 𝜅𝜔𝜍𝜀:
            return λ𝜏𝛽⇕
        𝝰𝝜𝜊 = 𝜅𝜔𝜍𝜀[0]
        if 𝝰𝝜𝜊 != '':
            return 𝛏𝜌𝜋𝜖𝛮(λ𝜏𝛽⇕ + [ƐϻϐϖϼϗϪ(𝝰𝝜𝜊)], 𝜅𝜔𝜍𝜀[1:])
        else:
            return 𝛏𝜌𝜋𝜖𝛮(λ𝜏𝛽⇕, 𝜅𝜔𝜍𝜀[1:])

    return 𝛏𝜌𝜋𝜖𝛮([], ら𝑫𝕀𝔾)