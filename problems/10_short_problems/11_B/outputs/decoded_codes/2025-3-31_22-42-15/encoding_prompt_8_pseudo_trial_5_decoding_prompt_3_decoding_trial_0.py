# Function to find a non-negative integer 'i' such that the sum of the first 'i' natural numbers
# meets a given condition relative to an input number 'n'
def find_integer_for_sum():
    # Step 2: Get Input
    desired_sum = abs(int(input()))  # Convert input to absolute integer

    # Step 3: Initialize a Counter
    i = 0  # Counter for the number of terms

    # Step 4: Loop Indefinitely
    while True:
        # Step 1a: Calculate the sum of the first 'i' natural numbers
        sum_of_first_i = (i * (i + 1)) // 2  # Use integer division for accuracy

        # Step 1b: Determine the difference
        difference = sum_of_first_i - desired_sum

        # Step 3: Check Conditions
        if sum_of_first_i == desired_sum:
            print(i)  # Output the found value of 'i'
            break  # Exit the loop

        if sum_of_first_i > desired_sum:
            if difference % 2 == 0:
                print(i)  # Output the found value of 'i' where the difference is even
                break  # Exit the loop

        # Step 4: Increment the Counter
        i += 1  # Move to the next integer

# Call the function to execute the algorithm
find_integer_for_sum()
