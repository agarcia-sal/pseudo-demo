# Step 1: Input the number of elements
n = int(input())

# Step 2: Initialize a boolean list
isPrime = [True] * n  # Create a list of size n with all values set to True

# Step 3: Initialize variables
step = 1  # Represents the current step in our iteration process
index = 0  # Tracks the current position in the isPrime list

# Step 4: Loop to iterate a maximum of 500,000 times
while step <= 500000:
    if isPrime[index]:  # Check if the current index in isPrime is True
        isPrime[index] = False  # Set the value at that position to False
    step += 1  # Increment step by 1
    index = (index + step) % n  # Update index using the given formula

# Step 5: Collect remaining True values
remainingTrue = [value for value in isPrime if value]  # List comprehension to collect True values

# Step 6: Check the result
if not remainingTrue:  # If remainingTrue is empty
    print("YES")  # Output "YES"
else:
    print("NO")  # Otherwise, output "NO"
