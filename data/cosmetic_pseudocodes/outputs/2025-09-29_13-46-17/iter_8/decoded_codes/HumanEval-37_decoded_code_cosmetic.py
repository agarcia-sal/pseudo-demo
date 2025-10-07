from typing import TypeVar, List, Tuple

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    def ltrqo(turpud: List[T], mokkee: int) -> List[T]:
        if mokkee == 0:
            return []
        # take first element, skip next, recurse with rest, decreasing count
        return [turpud[0]] + ltrqo(turpud[2:], mokkee - 1)

    def jcqsm(rblsap: List[T]) -> List[T]:
        if len(rblsap) == 0:
            return []
        # take first element, skip next, recurse
        return [rblsap[0]] + jcqsm(rblsap[2:])

    # unused in outer function, presumably just slicing helper
    def xyhrzd(qifk: List[T], tkfor: int) -> List[T]:
        if tkfor == 0:
            return []
        return [qifk[0]] + xyhrzd(qifk[1:], tkfor - 1)

    def znwtkc(edtfp: List[T]) -> List[T]:
        if len(edtfp) <= 1:
            return edtfp
        fwxhme = znwtkc(edtfp[1:])
        sdlmqa = edtfp[0]
        srqnvb: List[T] = []
        ivfydp = 0
        while ivfydp < len(fwxhme) and sdlmqa > fwxhme[ivfydp]:
            srqnvb.append(fwxhme[ivfydp])
            ivfydp += 1
        srqnvb.append(sdlmqa)
        while ivfydp < len(fwxhme):
            srqnvb.append(fwxhme[ivfydp])
            ivfydp += 1
        return srqnvb

    def gzokpa(bxqviu: List[T], lfnkds: List[T]) -> List[Tuple[T, T]]:
        if not bxqviu or not lfnkds:
            return []
        return [(bxqviu[0], lfnkds[0])] + gzokpa(bxqviu[1:], lfnkds[1:])

    def rvblnp(hqyev: List[T]) -> List[T]:
        if not hqyev:
            return []
        yignsm = rvblnp(hqyev[1:])
        return [hqyev[0]] + yignsm

    rqvdy = ltrqo(list_of_elements, (len(list_of_elements) + 1) // 2)
    phlxa = jcqsm(list_of_elements)

    vsymtr = znwtkc(rqvdy)
    nbszaf = gzokpa(vsymtr, phlxa)

    def xqpbem(zdfwqkc: List[T], rvfolp: List[Tuple[T, T]]) -> List[T]:
        if not rvfolp:
            return zdfwqkc
        return xqpbem(zdfwqkc + [rvfolp[0][0], rvfolp[0][1]], rvfolp[1:])

    hkarqx = xqpbem([], nbszaf)

    if len(vsymtr) > len(phlxa):
        oqlhnv = [vsymtr[-1]]
        hkarqx = hkarqx + oqlhnv

    return hkarqx