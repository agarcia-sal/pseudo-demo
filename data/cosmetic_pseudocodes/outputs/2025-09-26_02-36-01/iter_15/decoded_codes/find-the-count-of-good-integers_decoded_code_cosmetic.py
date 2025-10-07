class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        qwy = []
        wjq = 0
        hbk = max((n - 1) // 2, 0)
        vqs = 10 ** hbk

        while wjq < n + 1:
            qlq = 1
            zmz = wjq
            while zmz > 1:
                qlq *= zmz
                zmz -= 1
            qwy.append(qlq)
            wjq += 1

        btu = 0
        yvz = set()
        ued = vqs

        while ued < vqs * 10:
            hzj = ""
            kzv = ued
            while kzv > 0:
                hzj = chr(48 + kzv % 10) + hzj
                kzv //= 10
            if hzj == "":
                hzj = "0"

            revhzj = hzj[::-1]
            hsx = revhzj[(n % 2):]
            tcz = hzj + hsx

            tfx = int(tcz)
            if (tfx % k) != 0:
                ued += 1
                continue

            hgl = sorted(list(tcz))
            tgr = "".join(hgl)

            if tgr in yvz:
                ued += 1
                continue
            yvz.add(tgr)

            ppu = {}
            for ch in tgr:
                ppu[ch] = ppu.get(ch, 0) + 1

            if '0' in ppu and ppu['0'] > 0:
                sod = n - ppu['0']
                res = sod * qwy[n - 1]  # factorial of (n - 1)
            else:
                res = qwy[n]  # factorial of n

            for vvk in ppu.values():
                res //= qwy[vvk]

            btu += res
            ued += 1

        return btu