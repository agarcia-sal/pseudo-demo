# Initialize Variables
n = int(input())
b = [True] * n
j = 0
i = 1

# Loop Through Indices
while i <= 500000:
    if b[j]:
        b[j] = False
    i += 1
    j = (j + i) % n

# Check Remaining True Values
x = [value for value in b if value]

# Output Result
if len(x) == 0:
    print("YES")
else:
    print("NO")
