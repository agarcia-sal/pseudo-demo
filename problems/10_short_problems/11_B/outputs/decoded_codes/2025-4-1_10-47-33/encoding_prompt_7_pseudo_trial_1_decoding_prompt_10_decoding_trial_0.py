def absolute_value(num):
    """Returns the absolute value of the given integer."""
    return abs(num)

def integer_input():
    """Prompts user for an integer input and returns its absolute value."""
    return absolute_value(int(input()))

def find_integer(n):
    """Finds and returns an integer i such that the sum of the first i integers 
       either equals or exceeds the input n in a specific manner."""
    # Take an absolute integer input
    n = absolute_value(n)
    
    # Initialize iteration variable
    i = 0
    
    while True:
        # Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2  # Using integer division
        
        # Calculate the difference between s and n
        m = s - n
        
        # Check if the calculated sum s is equal to n
        if s == n:
            print(i)  # Print the integer i
            break  # Exit the loop

        # Check if the calculated sum s is greater than n
        elif s > n:
            # Check if the difference m is even
            if m % 2 == 0:
                print(i)  # Print the integer i
                break  # Exit the loop
        
        # Increment i for the next iteration
        i += 1

# To invoke the function in a typical use case
if __name__ == "__main__":
    n = integer_input()  # Get input from user
    find_integer(n)
