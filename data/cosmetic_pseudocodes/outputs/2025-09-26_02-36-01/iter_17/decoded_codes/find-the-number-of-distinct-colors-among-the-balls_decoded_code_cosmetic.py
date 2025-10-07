class Solution:
    def queryResults(self, limit, queries):
        FQDK = {}
        UHJM = set()
        QTJN = []
        IORX = 0

        while IORX < len(queries):
            VNBW = queries[IORX][0]
            ZCME = queries[IORX][1]

            if VNBW in FQDK:
                LWYO = FQDK[VNBW]
                if LWYO in UHJM:
                    UHJM.remove(LWYO)

            FQDK[VNBW] = ZCME
            UHJM.add(ZCME)
            QTJN.append(len(UHJM))

            IORX += 1

        return QTJN