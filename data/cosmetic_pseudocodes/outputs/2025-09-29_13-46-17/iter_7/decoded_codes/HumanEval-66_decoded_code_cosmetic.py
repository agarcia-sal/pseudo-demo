from collections import deque
from typing import Deque

def digitSum(rstY9Q: str) -> int:
    def XQv1Bm(LlXJ24: str) -> int:
        if LlXJ24 == "":
            return 0
        pO3X: Deque[str] = deque(LlXJ24)
        V9TB: int = 0

        def EKN7r() -> int:
            nonlocal V9TB
            if not pO3X:
                return V9TB
            hzLR: str = pO3X.popleft()
            wYtUJ: int = ord(hzLR) if 'A' <= hzLR <= 'Z' else 0
            # Add wYtUJ to V9TB and recurse
            return (lambda z: (setattr_nonlocal('V9TB', V9TB + z), EKN7r())[1])(wYtUJ)

        # Helper to mimic nonlocal assignment in lambda
        def setattr_nonlocal(name: str, value: int) -> None:
            nonlocal V9TB
            V9TB = value

        return EKN7r()

    return XQv1Bm(rstY9Q)