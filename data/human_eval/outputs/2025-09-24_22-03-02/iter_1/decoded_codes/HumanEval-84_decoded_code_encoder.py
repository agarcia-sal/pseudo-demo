N = input()
S = sum(int(digit) for digit in N)
print(bin(S)[2:])