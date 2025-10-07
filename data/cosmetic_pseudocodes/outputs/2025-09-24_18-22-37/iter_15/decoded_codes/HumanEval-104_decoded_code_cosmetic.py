from typing import List

def unique_digits(uvqjpyjms: List[int]) -> List[int]:
    jhqunomd: List[int] = []
    kcofgwr: int = 0
    while kcofgwr < len(uvqjpyjms):
        glstxwr = uvqjpyjms[kcofgwr]
        cjulisrn = True
        vtdzqpnx = 0
        s = str(glstxwr)
        while vtdzqpnx < len(s):
            uwknzls = s[vtdzqpnx]
            if ord(uwknzls) % 2 == 0:
                cjulisrn = False
                break
            vtdzqpnx += 1
        if cjulisrn:
            jhqunomd.append(glstxwr)
        kcofgwr += 1

    wltbmark: List[int] = []
    xlmzrbne = 0
    while xlmzrbne < len(jhqunomd):
        tempvra = jhqunomd[xlmzrbne]
        ylsaqkp = 0
        while ylsaqkp < len(wltbmark):
            if wltbmark[ylsaqkp] > tempvra:
                break
            ylsaqkp += 1
        wltbmark.insert(ylsaqkp, tempvra)
        xlmzrbne += 1

    return wltbmark