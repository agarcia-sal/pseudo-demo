# Start
# Input the absolute value of an integer
n = abs(int(input()))

# Initialize index variable
i = 0

# Loop indefinitely
while True:
    # Calculate the sum of the first i integers
    s = (i * (i + 1)) // 2
    
    # Calculate the difference between the sum and n
    m = s - n
    
    # Check if the sum equals n
    if s == n:
        print(i)
        break
    
    # Check if the sum is greater than n
    if s > n:
        # Check if the difference m is even
        if m % 2 == 0:
            print(i)
            break
    
    # Increment the index variable
    i += 1
# End
