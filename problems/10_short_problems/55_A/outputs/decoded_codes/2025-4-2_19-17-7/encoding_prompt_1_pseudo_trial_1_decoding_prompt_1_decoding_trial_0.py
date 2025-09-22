# 1. Input the number of elements
n = int(input())

# 2. Initialize a boolean list
isPrime = [True] * n

# 3. Initialize variables
step = 1
index = 0

# 4. Loop to iterate a maximum of 500,000 times
while step <= 500000:
    # If the value at the current index in isPrime is True
    if isPrime[index]:
        # Set the value at that position in isPrime to False
        isPrime[index] = False
    
    # Increment step by 1
    step += 1
    
    # Update the index to the next position using the formula
    index = (index + step) % n

# 5. Collect remaining True values
remainingTrue = [i for i in isPrime if i]

# 6. Check the result
if not remainingTrue:
    print("YES")
else:
    print("NO")
