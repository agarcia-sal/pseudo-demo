from typing import List

def words_string(input_string: str) -> List[str]:
    def ♗₇✘㊊(i: str, j: str) -> str:
        if i == j:
            return ''
        first_char = i[0]
        c = ' ' if first_char == ',' else first_char
        return c + ♗₇✘㊊(i[1:], j)

    𝒳𝒴𝒵 = ♗₇✘㊊(input_string, input_string)

    def 𝓦𝓕𝓤𝓟(s: List[str], ᖷ: str) -> List[str]:
        if ᖷ == '':
            return []
        first_split = ''
        first_index = 0
        while first_index < len(ᖷ) and ᖷ[first_index] != ' ':
            first_split += ᖷ[first_index]
            first_index += 1
        rest = ᖷ[first_index+1:] if first_index + 1 <= len(ᖷ) else ''
        return s + [first_split] + 𝓦𝓕𝓤𝓟(s + [first_split], rest)

    𝓥𝓛𝓗: List[str] = []
    𝓤𝓜𝓐 = 0
    while 𝓤𝓜𝓐 < len(𝒳𝒴𝒵):
        if 𝒳𝒴𝒵[𝓤𝓜𝓐] != ' ' and 𝓤𝓜𝓐 == 0:
            𝓥𝓛𝓗.append(GET_WORD(𝒳𝒴𝒵, 𝓤𝓜𝓐))
        elif 𝒳𝒴𝒵[𝓤𝓜𝓐] == ' ':
            𝓥𝓛𝓗.append(GET_WORD(𝒳𝒴𝒵, 𝓤𝓜𝓐 + 1))
        𝓤𝓜𝓐 += 1

    return SPLIT_ON_SPACE(𝒳𝒴𝒵)

def GET_WORD(𝓟: str, 𝓠: int) -> str:
    𝓡 = ''
    while 𝓠 < len(𝓟) and 𝓟[𝓠] != ' ':
        𝓡 += 𝓟[𝓠]
        𝓠 += 1
    return 𝓡

def SPLIT_ON_SPACE(𝓧: str) -> List[str]:
    𝓨: List[str] = []
    𝓩 = ''
    for 𝓪 in 𝓧:
        if 𝓪 == ' ':
            if 𝓩 != '':
                𝓨.append(𝓩)
                𝓩 = ''
        else:
            𝓩 += 𝓪
    if 𝓩 != '':
        𝓨.append(𝓩)
    return 𝓨