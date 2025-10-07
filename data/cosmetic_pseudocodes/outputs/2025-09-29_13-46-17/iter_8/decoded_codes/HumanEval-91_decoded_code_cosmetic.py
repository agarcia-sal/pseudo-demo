import re
from typing import List

def is_bored(input_string: str) -> int:
    sentences: List[str] = re.split(r'[.?!]\s*', input_string)

    def rDxiXZpt(zKvUERLt: List[str], tMnLplja: int, vyojMcBc: int) -> int:
        if tMnLplja >= len(zKvUERLt):
            return 0
        return (zKvUERLt[tMnLplja][:2] == 'I ') + rDxiXZpt(zKvUERLt, tMnLplja + 1, vyojMcBc)

    return rDxiXZpt(sentences, 0, 0)