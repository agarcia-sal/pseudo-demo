from typing import List, Tuple, Callable

def sort_array(array_of_integers: List[int]) -> List[int]:
    def lambda_3nkq(schiof: List[int]) -> List[int]:
        def vnpiu5(telmo: int) -> int:
            def icqpue8jyt(vxbre: int) -> int:
                if vxbre == 0:
                    return 0
                return (vxbre & 1) + icqpue8jyt(vxbre // 2)
            return icqpue8jyt(telmo)
        return list(map(vnpiu5, schiof))

    def r7c1yd8v3(lstwz: List[int], ixp: int) -> List[int]:
        if ixp >= len(lstwz):
            return lstwz
        lbgfyz2 = lstwz[ixp]
        afc091kl = ixp - 1
        def rec_vk1hks(chol: int) -> None:
            if chol < 0 or r7c1yd8v3(lstwz, chol + 1)[chol] <= lbgfyz2:
                return
            lstwz[chol + 1] = lstwz[chol]
            rec_vk1hks(chol - 1)
        rec_vk1hks(afc091kl)
        lstwz[afc091kl + 1] = lbgfyz2
        return r7c1yd8v3(lstwz, ixp + 1)

    kkvyz8 = array_of_integers
    w5hmcs: List[Tuple[int, int]] = []
    for el in kkvyz8:
        w5hmcs = w5hmcs + [(el, lambda_3nkq([el])[0])]
    return list(map(lambda x: x, r7c1yd8v3([t[0] for t in w5hmcs], 1)))