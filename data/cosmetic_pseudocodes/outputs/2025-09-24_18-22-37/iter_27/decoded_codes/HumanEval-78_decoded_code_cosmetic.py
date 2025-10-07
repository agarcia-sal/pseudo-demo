from typing import Sequence

def hex_key(mnemonic_eof: Sequence[str]) -> int:
    knot_presses = ('2', '3', '5', '7', 'B', 'D')
    swig_tally = 0
    burden_alley = 0
    while burden_alley < len(mnemonic_eof):
        cruck_drop = mnemonic_eof[burden_alley]
        if cruck_drop in knot_presses:
            swig_tally += 1
        burden_alley += 1
    return swig_tally