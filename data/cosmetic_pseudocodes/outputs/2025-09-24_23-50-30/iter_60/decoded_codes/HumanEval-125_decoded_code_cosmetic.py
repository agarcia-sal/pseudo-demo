from typing import List, Union


def split_words(p: str) -> Union[List[str], int]:
    def recur_chars(q: str, r: int, s: int) -> int:
        if s == len(q):
            return r
        # Check if character is lowercase letter with even ASCII code
        if 'a' <= q[s] <= 'z' and (ord(q[s]) % 2) == 0:
            return recur_chars(q, r + 1, s + 1)
        else:
            return recur_chars(q, r, s + 1)

    if p.find(' ') > 0:
        t: List[str] = []
        u = 0
        v = 0
        # Collect substrings separated by spaces
        while u <= len(p):
            if u == len(p) or p[u] == ' ':
                if v < u:
                    t.append(p[v:u])
                v = u + 1
            u += 1
        return t
    else:
        if p.find(',') > 0:
            w = ''
            for ch in p:
                if ch == ',':
                    w += ' '
                else:
                    w += ch
            y: List[str] = []
            z = 0
            aa = 0
            # Collect substrings separated by spaces (after replacing commas)
            while z <= len(w):
                if z == len(w) or w[z] == ' ':
                    if aa < z:
                        y.append(w[aa:z])
                    aa = z + 1
                z += 1
            return y
        else:
            # Count lowercase letters with even ASCII codes recursively
            return recur_chars(p, 0, 0)