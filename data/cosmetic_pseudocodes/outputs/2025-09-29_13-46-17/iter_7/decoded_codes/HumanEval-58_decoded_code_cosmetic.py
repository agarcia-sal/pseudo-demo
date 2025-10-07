from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, value: int, next: Optional[ListNode] = None) -> None:
        self.value: int = value
        self.next: Optional[ListNode] = next


def common(alpha: Optional[ListNode], bravo: Optional[ListNode]) -> Optional[ListNode]:
    # Reverses a list into l4M accumulator (not used directly outside)
    def _s44k(W72: Optional[ListNode], l4M: Optional[ListNode]) -> Optional[ListNode]:
        if W72 is None:
            return l4M
        return _s44k(W72.next, ListNode(W72.value, l4M))

    # Filters bravo to retain only nodes with value == x0l and merges into Uz5; 
    # traverses OMP recursively, calling _pE2j for each value of OMP
    def _kj8t(OMP: Optional[ListNode], x0l: int, Uz5: Optional[ListNode]) -> Optional[ListNode]:
        if OMP is None:
            return Uz5

        def _pE2j(Ak7: Optional[ListNode], UG3: int, Vlq: Optional[ListNode]) -> Optional[ListNode]:
            if Ak7 is None:
                return Vlq
            if not (Ak7.value != UG3):  # i.e. Ak7.value == UG3
                return _pE2j(Ak7.next, UG3, ListNode(x0l, Vlq))
            else:
                return _pE2j(Ak7.next, UG3, Vlq)

        return _kj8t(OMP.next, x0l, _pE2j(bravo, x0l, Uz5))

    # Copies list Mr8 recursively, returns new list in same order
    def _Zuw(Mr8: Optional[ListNode]) -> Optional[ListNode]:
        if Mr8 is None:
            return None
        if Mr8.next is not None:
            return ListNode(Mr8.value, _Zuw(Mr8.next))
        else:
            return ListNode(Mr8.value, None)

    # Reverses list L2W into a new list and then returns a copy of that reversed list
    def _ueM(L2W: Optional[ListNode]) -> Optional[ListNode]:
        def _d3g(KL1: Optional[ListNode], sBA: Optional[ListNode]) -> Optional[ListNode]:
            if KL1 is None:
                return _Zuw(sBA)
            return _d3g(KL1.next, ListNode(KL1.value, sBA))
        return _d3g(L2W, None)

    # Copies list fRv recursively, returns new list in same order
    def _B0v(fRv: Optional[ListNode]) -> Optional[ListNode]:
        if fRv is None:
            return None
        if fRv.next is not None:
            return ListNode(fRv.value, _B0v(fRv.next))
        else:
            return ListNode(fRv.value, None)

    # Filters listB to contain only those nodes whose values appear in bravo
    def _EHn(listB: Optional[ListNode]) -> Optional[ListNode]:
        def _PvW(yZP: int, JhC: Optional[ListNode]) -> Optional[ListNode]:
            if JhC is None:
                return None
            if yZP == JhC.value:
                return ListNode(JhC.value, _PvW(yZP, JhC.next))
            else:
                return _PvW(yZP, JhC.next)

        if listB is None:
            return None
        if _PvW(listB.value, bravo) is not None:
            return ListNode(listB.value, _EHn(listB.next))
        else:
            return _EHn(listB.next)

    zQ9xr = _EHn(alpha)
    return _B0v(zQ9xr)