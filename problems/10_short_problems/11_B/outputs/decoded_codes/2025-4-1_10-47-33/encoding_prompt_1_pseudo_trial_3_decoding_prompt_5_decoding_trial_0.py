def find_special_integer():
    # Initialize n to the absolute value of the integer input
    n = abs(int(input()))
    # Set i to 0; this will be used to calculate the sequence
    i = 0

    while True:  # Start an infinite loop
        # Calculate s as the sum of the first i natural numbers
        s = i * (i + 1) // 2
        # Calculate m as s - n
        m = s - n
        
        # Check if s is equal to n
        if s == n:
            print(i)  # Print the value of i
            break  # Exit the loop
        
        # Check if s is greater than n
        if s > n:
            # Check if m is an even number
            if m % 2 == 0:
                print(i)  # Print the value of i
                break  # Exit the loop
        
        # Increment the value of i to check the next number in the sequence
        i += 1

# Example test case usage
# find_special_integer()  # Uncomment this line to test the function
