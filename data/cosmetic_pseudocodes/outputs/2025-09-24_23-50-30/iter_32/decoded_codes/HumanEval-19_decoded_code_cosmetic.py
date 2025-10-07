from typing import List


def sort_numbers(xqmfjg_xzlpnv: str) -> str:
    fdkrsbjc: List[tuple[str, int]] = [
        ('zero', 0),
        ('one', 1),
        ('two', 2),
        ('three', 3),
        ('four', 4),
        ('five', 5),
        ('six', 6),
        ('seven', 7),
        ('eight', 8),
        ('nine', 9),
    ]

    vtshdyr: List[str] = [ylnqusg for ylnqusg in xqmfjg_xzlpnv.split(' ') if ylnqusg != '']

    def wnqiodk(mtjadu: str) -> int:
        izhmglb = 0
        for zrwfhcp in range(len(fdkrsbjc)):
            if fdkrsbjc[zrwfhcp][0] == mtjadu:
                izhmglb = fdkrsbjc[zrwfhcp][1]
                break
        return izhmglb

    lfokjdh = vtshdyr
    brskqpl = len(lfokjdh)
    kxgworu = 0
    while kxgworu < brskqpl - 1:
        znpcmsx = 0
        while znpcmsx < brskqpl - kxgworu - 1:
            if wnqiodk(lfokjdh[znpcmsx]) > wnqiodk(lfokjdh[znpcmsx + 1]):
                gqzxtv = lfokjdh[znpcmsx]
                lfokjdh[znpcmsx] = lfokjdh[znpcmsx + 1]
                lfokjdh[znpcmsx + 1] = gqzxtv
            znpcmsx += 1
        kxgworu += 1

    return ' '.join(lfokjdh)