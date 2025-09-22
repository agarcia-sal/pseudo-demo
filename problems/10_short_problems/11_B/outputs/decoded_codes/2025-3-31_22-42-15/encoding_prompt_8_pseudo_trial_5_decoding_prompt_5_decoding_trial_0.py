# Function to find a non-negative integer 'i' such that sum of first 'i' natural numbers either equals or can be adjusted to equal a given number 'n'
def find_integer_for_sum():
    # Get input from the user and convert it to an absolute integer
    desired_sum = abs(int(input()))
    
    # Initialize a counter for the current integer 'i'
    i = 0
    
    # Loop indefinitely until a valid 'i' is found
    while True:
        # Calculate the sum of the first 'i' natural numbers using the formula
        sum_of_first_i = (i * (i + 1)) // 2
        
        # Determine the difference between the calculated sum and the desired sum
        difference = sum_of_first_i - desired_sum
        
        # Check the conditions
        if sum_of_first_i == desired_sum:
            print(i)  # Print 'i' if it matches the desired sum
            break
        elif sum_of_first_i > desired_sum:
            if difference % 2 == 0:
                print(i)  # Print 'i' if the difference is even
                break
        
        # Increment the counter for the next integer
        i += 1

# Invoke the function to execute
find_integer_for_sum()
