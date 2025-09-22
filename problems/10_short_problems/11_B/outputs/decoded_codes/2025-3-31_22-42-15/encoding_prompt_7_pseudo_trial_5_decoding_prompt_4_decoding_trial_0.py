def find_integer():
    n = abs(int(input()))  # Convert input to an absolute integer
    i = 0  # Initialize a counter

    while True:  # Start an infinite loop
        s = (i * (i + 1)) // 2  # Calculate the sum of the first i natural numbers
        m = s - n  # Determine the difference between the sum and n
        
        if s == n:  # Check if the sum equals n
            print(i)  # Print the current value of i
            break  # Exit the loop
        
        elif s > n:  # Check if the sum is greater than n
            if m % 2 == 0:  # Check if the difference is even
                print(i)  # Print the current value of i
                break  # Exit the loop
        
        i += 1  # Increment the counter for the next iteration

# Example of how to call the function (uncomment the line below to run):
# find_integer()
