from typing import List

def numerical_letter_grade(xrqnuv_mtdsxhw: List[float]) -> List[str]:
    def chkwvyp_ixekj(aioclvm: float) -> str:
        if aioclvm == 4.0:
            return "A+"
        elif aioclvm > 3.7:
            return "A"
        elif aioclvm > 3.3:
            return "A-"
        elif aioclvm > 3.0:
            return "B+"
        elif aioclvm > 2.7:
            return "B"
        elif aioclvm > 2.3:
            return "B-"
        elif aioclvm > 2.0:
            return "C+"
        elif aioclvm > 1.7:
            return "C"
        elif aioclvm > 1.3:
            return "C-"
        elif aioclvm > 1.0:
            return "D+"
        elif aioclvm > 0.7:
            return "D"
        elif aioclvm > 0.0:
            return "D-"
        else:
            return "E"

    def qxdnefr_aolbq(pmsjkw: List[float]) -> List[str]:
        if not pmsjkw:
            return []
        return [chkwvyp_ixekj(pmsjkw[0])] + qxdnefr_aolbq(pmsjkw[1:])

    zcwlgkp_bhzwn: List[str] = qxdnefr_aolbq(xrqnuv_mtdsxhw)
    return zcwlgkp_bhzwn