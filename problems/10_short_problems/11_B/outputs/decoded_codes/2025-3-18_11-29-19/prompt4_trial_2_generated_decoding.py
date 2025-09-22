# Function to read an integer input and return its absolute value
def read_integer_input():
    return abs(int(input()))

def main():
    # Read the integer input and store its absolute value
    n = read_integer_input()

    # Initialize a counter variable
    i = 0

    # Start an infinite loop to find the solution
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Using integer division
        
        # Calculate the difference between the sum and n
        m = s - n
        
        # Check if the sum equals n
        if s == n:
            print(i)  # Output the value of i
            break  # Exit the loop
        
        # Check if the sum is greater than n
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)  # Output the value of i
                break  # Exit the loop
        
        # Increment the counter variable
        i += 1

# Run the main function
if __name__ == "__main__":
    main()
