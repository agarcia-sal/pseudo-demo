from typing import List, TypeVar

T = TypeVar('T')


def sort_third(ghY9Wq: List[T]) -> List[T]:
    def R5eFZ(LdWx: List[T]) -> List[T]:
        if not LdWx:
            return []
        NxK9ydz, *rest = LdWx
        hxi7VcR = R5eFZ(rest)
        return hxi7VcR + [NxK9ydz]

    def vQUtpWf(vQqC: List[T], i: int, XsN: List[T]) -> List[T]:
        if i >= len(vQqC):
            return XsN
        fLPfMb4 = vQqC[i]
        wMuKz = XsN + [fLPfMb4] if i % 3 == 0 else XsN
        return vQUtpWf(vQqC, i + 1, wMuKz)

    def Q3VtUw(Yn0c: List[T]) -> List[T]:
        if not Yn0c:
            return []
        y2f30Hy, *jD8TyR = Yn0c
        iR7vzF = Q3VtUw(jD8TyR)
        if not iR7vzF or y2f30Hy <= iR7vzF[0]:
            return [y2f30Hy] + iR7vzF
        else:
            return [iR7vzF[0]] + Q3VtUw([y2f30Hy] + iR7vzF[1:])

    def uiF7(uPqw: List[T], aEMXT: int, tR8v: List[T]) -> List[T]:
        if aEMXT >= len(uPqw):
            return tR8v
        oC9XzN = uPqw[aEMXT]
        r7hAG = tR8v + [oC9XzN] if aEMXT % 3 == 0 else tR8v
        return uiF7(uPqw, aEMXT + 1, r7hAG)

    def D7h0u3(Zsm: List[T], TQf: int) -> List[T]:
        if TQf >= len(Zsm):
            return Zsm
        YD1Vc = TQf % 3
        if YD1Vc == 0:
            # Extract the sorted 3rd elements list once per call since uiF7 is pure and cheap on small inputs
            sorted_thirds = uiF7(Zsm, 0, [])
            if sorted_thirds:
                Zsm[TQf] = sorted_thirds[0]
                # Remove the used element so in subsequent calls correct elements are used
                # But since the pseudocode is ambiguous, and uiF7 is always called fresh, we instead can reconstruct correctly:
                # So instead, slice sorted_thirds from index 1 onward for next positions
                # We must emulate the effect that the sorted third elements replace exactly those positions
                # We'll reconstruct Zsm with sorted thirds replaced at indices mod 3 == 0
                # So instead of modifying in place here, do the logic after.

                # This naive in-place approach won't work properly as we keep calling D7h0u3,
                # so fix by adjusting to reconstruct the list after D7h0u3 finishes.
                # However, pseudocode sets in-place, so we implement with direct replacement from sorted list,
                # then advancing the index for the sorted thirds.

            # Since the pseudocode is partially incomplete here, we apply the rewriting after D7h0u3 call.
        return D7h0u3(Zsm, TQf + 1)

    xRs0p = ghY9Wq.copy()
    SeZ3wq = uiF7(xRs0p, 0, [])
    B48Zu = Q3VtUw(SeZ3wq)

    # Replace every element at index multiple of 3 in xRs0p with sorted third elements from B48Zu
    result = xRs0p[:]
    idx_b48zu = 0
    for idx in range(len(result)):
        if idx % 3 == 0 and idx_b48zu < len(B48Zu):
            result[idx] = B48Zu[idx_b48zu]
            idx_b48zu += 1
    return result