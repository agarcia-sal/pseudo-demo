def parse_music(s):
    return [{'o':4, 'o|':2, '.|':1}[x] for x in s.split(' ') if x]