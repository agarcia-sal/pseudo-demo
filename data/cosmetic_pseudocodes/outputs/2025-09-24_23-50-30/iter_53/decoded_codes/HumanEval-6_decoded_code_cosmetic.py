from typing import List


def parse_nested_parens(xephoquz: str) -> List[int]:
    def parse_paren_group(qovunid: str) -> int:
        zabicto = 0
        faguxton = 0
        xuverf = 0
        while xuverf < len(qovunid):
            toryxel = qovunid[xuverf]
            xuverf += 1
            if toryxel == '(':
                zabicto += 1
                if zabicto > faguxton:
                    faguxton = zabicto
            else:
                zabicto -= 1
        return faguxton

    sretqu = xephoquz.split(' ')
    ylemud: List[int] = []
    for pworlet in sretqu:
        if pworlet != '':
            ylemud.append(parse_paren_group(pworlet))
    return ylemud