# Start of the program

# Importing necessary library for absolute value (optional, but for clarity)
# In Python, we can directly use the built-in abs() function.
# Define the main function to encapsulate the logic.
def main():
    # Get the absolute value of a number input from the user
    userInput = input()
    n = abs(int(userInput))  # Convert user input to integer and get the absolute value
    i = 0  # Initialize an index variable

    while True:  # Infinite loop
        # Calculate the sum of the first `i` integers using the formula
        sumOfFirsti = (i * (i + 1)) // 2  # Using integer division

        # Calculate the difference between the sum and n
        difference = sumOfFirsti - n

        # Check if the sum equals n
        if sumOfFirsti == n:
            print(i)  # Print the value of i
            break  # Exit the loop

        # Check if the sum is greater than n
        elif sumOfFirsti > n:
            # Check if the difference is even
            if difference % 2 == 0:  # Use modulus to check for even
                print(i)  # Print the value of i
                break  # Exit the loop

        # Increment i for the next iteration
        i += 1

# Call the main function to run the program
main()
