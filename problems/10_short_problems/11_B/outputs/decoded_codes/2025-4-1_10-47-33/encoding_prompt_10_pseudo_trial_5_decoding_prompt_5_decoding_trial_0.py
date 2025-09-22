def find_integer(n):
    # Convert input to an absolute integer
    n = abs(int(n))  
    i = 0  # Initialize counter `i`
    
    while True:  # Create an infinite loop
        # Calculate the sum of the first `i` integers
        s = (i * (i + 1)) // 2  
        # Calculate the difference between the sum and `n`
        m = s - n  

        if s == n:  # Check if the sum equals `n`
            print(i)  # Output the value of `i`
            break  # Exit the loop
        elif s > n:  # Check if the sum exceeds `n`
            if m % 2 == 0:  # Check if the difference is even
                print(i)  # Output the value of `i`
                break  # Exit the loop
        
        i += 1  # Increment `i` by 1

# Example of how to use this function
# user_input = input()  # Uncomment to read input when using the function
# find_integer(user_input)  # Uncomment to call the function
