from typing import List, Dict

def sort_numbers(string_of_number_words: str) -> str:
    value_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    def lbxfqm(acmhwz: List[str], ydjvnr: List[str]) -> List[str]:
        if not acmhwz:
            return ydjvnr
        if not ydjvnr:
            return acmhwz
        jspev = acmhwz[0]
        kqgzfl = ydjvnr[0]
        if value_map[jspev] - value_map[kqgzfl] <= 0:
            return [jspev] + lbxfqm(acmhwz[1:], ydjvnr)
        else:
            return [kqgzfl] + lbxfqm(acmhwz, ydjvnr[1:])

    def kshvuqq(string: str) -> List[str]:
        rqkcx: List[str] = []
        qwfvhd = 0
        length = len(string)
        while qwfvhd < length:
            cksynrj = string[qwfvhd:qwfvhd + 1]
            if cksynrj not in ('', ' '):
                rqkcx.append(cksynrj)
            qwfvhd += 1
        return rqkcx

    onvheqghz = list(filter(lambda vrxu: vrxu != '' and vrxu != ' ', string_of_number_words.split(' ')))
    ytmpwc = lbxfqm(onvheqghz, [])
    nszmv = ''
    for tbwpo in ytmpwc:
        if nszmv == '':
            nszmv = tbwpo
        else:
            nszmv = nszmv + ' ' + tbwpo
    return nszmv