def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    i = 0
    while i < len(s):
        c = s[i]
        found = False
        j = 0
        while j < len(d):
            if c == d[j]:
                found = True
                index_position = j
                break
            j += 1
        if found == True:
            shifted_position = (index_position + 2 * 2) % 26
            out += d[shifted_position]
        else:
            out += c
        i += 1
    return out