def main():
    # Read an integer input and store its absolute value
    input_number = abs(int(input()))
    index = 0

    # Infinite loop until a break condition is met
    while True:
        # Calculate the sum of the first 'index' integers
        total_sum = (index * (index + 1)) // 2
        
        # Calculate difference between sum and input_number
        difference = total_sum - input_number

        # Check if the sum equals the input_number
        if total_sum == input_number:
            print(index)
            break

        # Check if the sum exceeds the input_number
        elif total_sum > input_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break

        # Increment index for the next iteration
        index += 1

if __name__ == "__main__":
    main()
