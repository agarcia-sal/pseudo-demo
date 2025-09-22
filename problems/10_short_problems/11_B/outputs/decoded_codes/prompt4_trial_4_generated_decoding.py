# Read the input value and convert it to a positive integer
n = abs(int(input()))

# Initialize the counter variable
i = 0

# Start an infinite loop to find the required value
while True:
    # Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2  # Using integer division
    
    # Calculate the difference between the sum and n
    m = s - n
    
    # Check if the sum equals n
    if s == n:
        print(i)  # Output the current value of i
        break  # Exit the loop
    
    # Check if the sum exceeds n
    elif s > n:
        # Check if the difference is even
        if m % 2 == 0:
            print(i)  # Output the current value of i
            break  # Exit the loop
    
    # Increment the counter for the next iteration
    i += 1
