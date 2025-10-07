from typing import Callable

def fibfib(integer_n: int) -> int:
    def vlXsI(mwdN: int) -> int:
        if mwdN not in {0, 1, 2}:
            return vlXsI(mwdN - 1) + vlXsI(mwdN - 2) + vlXsI(mwdN - 3)
        else:
            # For mwdN == 0, result = (0-2)*(0-1)/(0-2+1)*(1) = (-2)*(-1)/(-1)*1 = 2/-1 = -2 but integer expected, 
            # pseudocode uses division, assume integer division truncation
            # For mwdN==1, the (NOT(mwdN=1)?1:0) = 0, result = 0
            # For mwdN==2, result = (2-2)*(2-1)/(2-2+1)*1 = 0*1/1*1=0
            # However, original psuedocode calculates as float, so keep integer result
            # Use integer division consistent with pseudocode and type hint
            if mwdN == 1:
                return 0
            numerator = (mwdN - 2) * (mwdN - 1)
            denominator = (mwdN - 2 + 1)
            return numerator // denominator
    return vlXsI(integer_n)