from typing import List

def words_string(input_string: str) -> List[str]:
    def aux(utz: int, acc: List[str]) -> List[str]:
        if utz == 0:
            return acc
        else:
            pqj = input_string[len(input_string) - utz]
            tgb = (pqj == ',')
            bxm = acc + [' '] if tgb else acc + [pqj]
            return aux(utz - 1, bxm)

    rfw = len(input_string)
    vkm = aux(rfw, [])
    djk = ''

    def cmb(xs: List[str], i: int, res: str) -> str:
        if i == len(xs):
            return res
        else:
            return cmb(xs, i + 1, res + xs[i])

    wpt = cmb(vkm, 0, djk)

    def zpq(s: str, idx: int, res_acc: List[str]) -> List[str]:
        if idx == len(s):
            return res_acc
        elif s[idx] == ' ':
            return zpq(s, idx + 1, res_acc + [''])
        else:
            hlt = len(res_acc)
            updated_word = res_acc[hlt - 1] + s[idx]
            return zpq(s, idx + 1, res_acc[:hlt - 1] + [updated_word])

    ntz: List[str] = zpq(wpt, 0, ['']) if wpt != '' else []
    return ntz