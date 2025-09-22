def main():
    # Step 1: Receive Input
    target_value = abs(int(input()))  # Read an integer and store its absolute value

    # Step 2: Initialize Counter
    index = 0

    # Step 3: Infinite Loop
    while True:
        # Step 3a: Calculate Triangle Number
        triangular_number = (index * (index + 1)) // 2  # Calculate triangular number using the formula

        # Step 3b: Calculate Difference
        difference = triangular_number - target_value  # Determine the difference

        # Step 3c: Check Conditions
        if triangular_number == target_value:
            print(index)  # Print index as the result
            break  # Exit the loop

        elif triangular_number > target_value:
            if difference % 2 == 0:  # Check if difference is even
                print(index)  # Print index as the result
                break  # Exit the loop

        # Step 3d: Increment Counter
        index += 1  # Increase index by 1

# Call the main function to run the program
if __name__ == "__main__":
    main()
