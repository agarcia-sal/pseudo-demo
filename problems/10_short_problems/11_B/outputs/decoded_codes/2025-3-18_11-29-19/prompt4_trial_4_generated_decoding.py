def absolute_value_of(value):
    # Function to return the absolute value of a number
    return abs(value)

def main():
    # Read input and convert it to an absolute integer
    number = absolute_value_of(int(input()))

    # Initialize counter index
    index = 0

    # Loop indefinitely
    while True:
        # Calculate the sum of the first 'index' integers using the formula: n(n+1)/2
        total_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the input number
        difference = total_sum - number

        # Check if the sum equals the input number
        if total_sum == number:
            # Print the current index
            print(index)
            break
        
        # Check if the sum exceeds the input number
        elif total_sum > number:
            # Check if the difference is even
            if difference % 2 == 0:
                # Print the current index
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1

# Run the main function
if __name__ == "__main__":
    main()
