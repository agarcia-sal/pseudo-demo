from typing import Set


def same_chars(alpha_37: str, beta_π: str) -> bool:
    xω9: Set[str] = set()
    yλσ: Set[str] = set()

    def Ω_extract(setξ: Set[str], strΙ: str) -> None:
        def Υ_recur(indexν: int) -> None:
            if indexν < 0:
                return
            setξ.add(strΙ[indexν])
            Υ_recur(indexν - 1)

        Υ_recur(len(strΙ) - 1)

    Ω_extract(xω9, alpha_37)
    Ω_extract(yλσ, beta_π)

    # Check that neither set excludes any element of the other (i.e., sets intersect fully)
    if not (xω9.isdisjoint(yλσ) is False and yλσ.isdisjoint(xω9) is False):
        # The original pseudocode tests EXCLUDES_ANY meaning no element of A in B.
        # So EXCLUDES_ANY corresponds to isdisjoint.
        # Then NOT (xω9.EXCLUDES_ANY(yλσ) OR yλσ.EXCLUDES_ANY(xω9)) means
        # neither is disjoint, so sets have some intersection.
        # So the condition is when both sets have some intersection.
        pass

    # Let's re-translate carefully:
    # IF NOT (xω9.EXCLUDES_ANY(yλσ) OR yλσ.EXCLUDES_ANY(xω9)) THEN RETURN TRUE ELSE FALSE
    # is the same as
    # Return not (xω9.excludes_any(yλσ) or yλσ.excludes_any(xω9))
    # EXCLUDES_ANY means the set excludes at least one element of the other. i.e. exists element in yλσ not in xω9.

    # So EXCLUDES_ANY means:
    # Does xω9 exclude any element of yλσ? i.e. Is there element in yλσ not in xω9? yλσ - xω9 != empty

    if (len(yλσ - xω9) == 0) and (len(xω9 - yλσ) == 0):
        return True
    else:
        return False