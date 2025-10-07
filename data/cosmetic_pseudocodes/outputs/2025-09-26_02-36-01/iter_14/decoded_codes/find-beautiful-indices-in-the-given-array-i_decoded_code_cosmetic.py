class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        list_xm = []
        len_sx = len(s)
        len_ax = len(a)
        rec_idx = 0
        while rec_idx <= len_sx - len_ax:
            if s[rec_idx:rec_idx + len_ax] == a:
                list_xm.append(rec_idx)
            rec_idx += 1

        list_yn = []
        len_bx = len(b)
        pointer_p = 0
        while pointer_p <= len_sx - len_bx:
            if s[pointer_p:pointer_p + len_bx] == b:
                list_yn.append(pointer_p)
            pointer_p += 1

        container_zq = []
        idx_outer = 0
        while idx_outer < len(list_xm):
            val_outer = list_xm[idx_outer]
            idx_inner = 0
            appended_flag = False
            while not appended_flag and idx_inner < len(list_yn):
                val_inner = list_yn[idx_inner]
                diff = val_outer - val_inner
                if -k <= diff <= k:
                    container_zq.append(val_outer)
                    appended_flag = True
                idx_inner += 1
            idx_outer += 1

        return container_zq