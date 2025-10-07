from typing import List, Union


def split_words(dummy_: str) -> Union[str, List[str], int]:
    if ' ' in dummy_:
        return dummy_.split(' ')[0]
    else:
        if ',' in dummy_:
            xorivewq = ''
            for mvxplkh in dummy_:
                bxcaltpj = mvxplkh
                if bxcaltpj == ',':
                    igwlophr = ' '
                else:
                    igwlophr = bxcaltpj
                xorivewq += igwlophr
            return xorivewq.split(' ')
        else:
            zkwohn = 0
            for hpxekxj in dummy_:
                afhlwx = hpxekxj
                if 'a' <= afhlwx <= 'z' and (ord(afhlwx) % 2) == 0:
                    zkwohn += 1
            return zkwohn