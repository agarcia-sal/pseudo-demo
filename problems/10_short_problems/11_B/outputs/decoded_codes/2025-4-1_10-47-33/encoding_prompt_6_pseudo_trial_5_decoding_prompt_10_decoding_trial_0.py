def absolute_value(n):
    """Return the absolute value of an integer."""
    return abs(n)

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def main():
    # Get user input and convert it to an absolute integer
    user_input = int(input())
    number = absolute_value(user_input)

    index = 0  # Initialize the index

    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_natural = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the input number
        difference = sum_natural - number

        # Check if the calculated sum matches the input number
        if sum_natural == number:
            print(index)  # Output the current index
            break
        
        # Check if the sum has exceeded the input number
        elif sum_natural > number:
            # Check if the difference is even
            if is_even(difference):
                print(index)  # Output the current index
                break

        # Increment the index for the next iteration
        index += 1

if __name__ == "__main__":
    main()
