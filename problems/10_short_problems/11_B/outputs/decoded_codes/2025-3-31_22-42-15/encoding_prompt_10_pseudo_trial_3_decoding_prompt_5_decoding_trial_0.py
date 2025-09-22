# Function to determine the value of i such that the sum of the first i natural numbers
# meets a certain condition relative to the absolute value of user input n.

def find_natural_sum_index():
    # Declare the variable n and take the absolute value of user input
    n = abs(int(input()))
    
    # Initialize the counter variable i
    i = 0
    
    # Start an infinite loop to find the correct value of i
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2
        # Calculate the difference between sum and n
        m = s - n
        
        # Check if the sum equals n
        if s == n:
            print(i)  # Output the value of i if the sum equals n
            break  # Exit the loop

        # Check if the sum is greater than n
        elif s > n:
            # Check if the difference m is even
            if m % 2 == 0:
                print(i)  # Output the value of i if m is even
                break  # Exit the loop
        
        # Increment i to check the next integer
        i += 1

# Call the function to execute
find_natural_sum_index()
