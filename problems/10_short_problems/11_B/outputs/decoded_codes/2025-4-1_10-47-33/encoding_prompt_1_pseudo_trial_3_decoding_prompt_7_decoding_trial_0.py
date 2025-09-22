# Initialize the variable n to the absolute value of the integer input
n = abs(int(input()))

# Set the variable i to 0 (this will be used to calculate a sequence)
i = 0

# Start an infinite loop to perform the following actions
while True:
    # Calculate s as the sum of the first i natural numbers
    s = i * (i + 1) // 2  # Using integer division to avoid float results
    # Calculate m as s - n
    m = s - n
    
    # Check if s is equal to n
    if s == n:
        print(i)  # Print the value of i
        break  # Exit the loop
    
    # Check if s is greater than n
    if s > n:
        # Check if m is an even number
        if m % 2 == 0:  # m is even
            print(i)  # Print the value of i
            break  # Exit the loop
    
    # Increment the value of i by 1 to check the next number in the sequence
    i += 1
