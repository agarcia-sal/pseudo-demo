# Step 1: Input the number of elements
n = int(input())

# Step 2: Initialize a boolean list
isPrime = [True] * n

# Step 3: Initialize variables
step = 1
index = 0

# Step 4: Loop to iterate a maximum of 500,000 times
while step <= 500000:
    if isPrime[index]:
        isPrime[index] = False
    step += 1
    index = (index + step) % n

# Step 5: Collect remaining True values
remainingTrue = [value for value in isPrime if value]

# Step 6: Check the result
if not remainingTrue:
    print("YES")
else:
    print("NO")
