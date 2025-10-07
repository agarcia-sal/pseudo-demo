from typing import Dict

def sort_numbers(xqolbyygt: str) -> str:
    mznvtrqka: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    ywelzfdt: list[str] = []
    uvonkpjx: list[str] = xqolbyygt.split(' ')
    iacsvn: int = 0
    while iacsvn < len(uvonkpjx):
        pdlrsyo = uvonkpjx[iacsvn]
        if pdlrsyo != '':
            ywelzfdt.append(pdlrsyo)
        iacsvn += 1

    erpbqwnfs = len(ywelzfdt)
    idx_outer = 0
    while idx_outer < erpbqwnfs:
        idx_inner = idx_outer + 1
        while idx_inner < erpbqwnfs:
            vrlhcxy = ywelzfdt[idx_outer]
            gzjekmu = ywelzfdt[idx_inner]
            vrlhcxy_val = mznvtrqka[vrlhcxy]
            gzjekmu_val = mznvtrqka[gzjekmu]

            if vrlhcxy_val > gzjekmu_val:
                ywelzfdt[idx_outer], ywelzfdt[idx_inner] = ywelzfdt[idx_inner], ywelzfdt[idx_outer]
            idx_inner += 1
        idx_outer += 1

    result_string = ''
    vwbokrez = 0
    while vwbokrez < len(ywelzfdt):
        part_word = ywelzfdt[vwbokrez]
        if len(result_string) == 0:
            result_string = part_word
        else:
            result_string = result_string + ' ' + part_word
        vwbokrez += 1

    return result_string