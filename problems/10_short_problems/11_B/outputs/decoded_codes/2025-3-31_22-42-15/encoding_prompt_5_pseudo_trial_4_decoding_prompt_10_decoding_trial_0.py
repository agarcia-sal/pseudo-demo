def main():
    # Step 2: Get user input and compute the absolute target value
    target_value = abs(int(input()))

    # Step 3: Initialize counter to 0
    counter = 0

    while True:
        # Step 4a: Calculate the triangular number
        triangular_number = (counter * (counter + 1)) // 2
        
        # Step 4b: Calculate the difference
        difference = triangular_number - target_value

        # Step 4c: Check if we found a match
        if triangular_number == target_value:
            print(counter)  # Found an exact match
            break  # Exit the loop

        # Step 4d: Check if triangular number is greater than target value
        elif triangular_number > target_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(counter)  # Found a conditional match
                break  # Exit the loop

        # Step 4e: Increment the counter
        counter += 1

# Start the program
if __name__ == "__main__":
    main()
