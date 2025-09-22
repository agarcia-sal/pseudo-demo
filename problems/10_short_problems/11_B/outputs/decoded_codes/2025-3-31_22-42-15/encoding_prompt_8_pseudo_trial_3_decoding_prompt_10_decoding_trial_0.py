def main():
    # Step 1: Get User Input
    target_value = int(input())
    target_value = abs(target_value)  # Calculate the absolute value of target_value

    # Step 2: Initialize Variables
    current_index = 0

    # Step 3: Begin Infinite Loop
    while True:
        # Calculate the sum of the first 'current_index' integers
        sum_of_integers = (current_index * (current_index + 1)) // 2  # Using integer division

        # Calculate the difference between sum_of_integers and target_value
        difference = sum_of_integers - target_value
        
        # Step 4: Check Conditions
        if sum_of_integers == target_value:
            print(current_index)  # Found the required index
            break  # Exit the loop
        
        if sum_of_integers > target_value:
            if difference % 2 == 0:  # Check if difference is evenly divisible by 2
                print(current_index)  # Found the required index
                break  # Exit the loop
        
        # Increment current_index for the next iteration
        current_index += 1

# Start the program
if __name__ == "__main__":
    main()
