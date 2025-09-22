def absolute_value(num):
    """Return the absolute value of the given number."""
    return -num if num < 0 else num

def sum_of_first_i_numbers(i):
    """Return the sum of the first i natural numbers."""
    return (i * (i + 1)) // 2  # Using integer division for clarity with // 

def main():
    # Take absolute value of user input and convert it to an integer
    n = absolute_value(int(input()))

    # Initialize a variable to keep track of the current number
    i = 0

    # Start an infinite loop for finding the required number
    while True:
        # Calculate the sum of the first i natural numbers
        s = sum_of_first_i_numbers(i)
        
        # Determine how much s exceeds n
        m = s - n
        
        # Check if the sum equals n
        if s == n:
            print(i)  # Print the current number i
            break
        
        # Check if the sum exceeds n
        elif s > n:
            # Check if the difference m is even
            if m % 2 == 0:
                print(i)  # Print the current number i
                break
        
        # Increment i for the next iteration
        i += 1

# Call the main function to execute the program
main()
