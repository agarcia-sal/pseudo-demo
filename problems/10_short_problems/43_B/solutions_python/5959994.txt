s1, s2 = [[x for x in y if x != ' '] for y in [input(), input()]]
freqs = [s1.count(chr(x)) - s2.count(chr(x)) for x in range(ord('A'), ord('z') + 1)]
print("YES" if len([x for x in freqs if x < 0]) == 0 else "NO")
