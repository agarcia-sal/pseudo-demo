from collections import defaultdict
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        vqr_ztb = defaultdict(int)  # dictionary_with_default_zero()

        def length_of(string: str) -> int:
            # Counting characters in the string
            pfx_rjg = 0
            while pfx_rjg < len(string):
                pfx_rjg += 1
            return pfx_rjg

        def substring_of(strng: str, start_idx: int, end_idx: int) -> str:
            # Return substring from start_idx (inclusive) to end_idx (exclusive)
            res = ""
            pos = start_idx
            while pos < end_idx:
                res += strng[pos]
                pos += 1
            return res

        def char_at(st: str, idx: int) -> str:
            return st[idx]

        # Populate frequency dictionary of all substrings from all strings in arr
        itr0 = 0
        while itr0 < length_of(arr):
            cbl_jvr = arr[itr0]
            len_agh = length_of(cbl_jvr)
            itr1 = 0
            while itr1 < len_agh:
                itr2 = itr1 + 1
                while itr2 <= len_agh:
                    sbv_ocz = substring_of(cbl_jvr, itr1, itr2)
                    vqr_ztb[sbv_ocz] += 1
                    itr2 += 1
                itr1 += 1
            itr0 += 1

        answer = []
        jdh_bgi = 0
        while jdh_bgi < length_of(arr):
            ltg_won = arr[jdh_bgi]
            uck_lph = length_of(ltg_won)
            yxs_qmr = ""
            jrt_bnv = 0
            while jrt_bnv < uck_lph:
                kxp_uls = jrt_bnv + 1
                while kxp_uls <= uck_lph:
                    bzr_qfp = substring_of(ltg_won, jrt_bnv, kxp_uls)
                    if vqr_ztb[bzr_qfp] == 1:
                        if (yxs_qmr == "") or (length_of(bzr_qfp) < length_of(yxs_qmr)) or \
                           ((length_of(bzr_qfp) == length_of(yxs_qmr)) and (bzr_qfp < yxs_qmr)):
                            yxs_qmr = bzr_qfp
                    kxp_uls += 1
                jrt_bnv += 1
            answer.append(yxs_qmr)
            jdh_bgi += 1

        return answer