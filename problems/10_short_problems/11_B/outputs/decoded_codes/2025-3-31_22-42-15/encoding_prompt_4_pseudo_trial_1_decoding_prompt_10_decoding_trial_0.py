def get_user_input():
    """Retrieve user input and convert it to an integer."""
    return abs(int(input()))

def find_integer(n):
    """Find the smallest integer i such that the sum of the first i integers equals n 
       or the difference between the sum and n is even."""
    i = 0  # Initialize variable to track the current number
    
    while True:  # Infinite loop to find the desired integer
        # Calculate the sum of the first 'i' integers using the formula sum = i * (i + 1) / 2
        sum_i = (i * (i + 1)) // 2
        
        # Calculate the difference between the sum and 'n'
        difference = sum_i - n
        
        # Check if the sum equals 'n'
        if sum_i == n:
            print(i)  # Output the current integer
            break  # Exit the loop
        
        # Check if the sum exceeds 'n'
        elif sum_i > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print(i)  # Output the current integer
                break  # Exit the loop
        
        # Increment 'i' for the next iteration
        i += 1

def main():
    """Main function to execute the program."""
    n = get_user_input()  # Get the absolute value of user input converted to integer
    find_integer(n)  # Find and print the integer

if __name__ == "__main__":
    main()  # Run the main function
