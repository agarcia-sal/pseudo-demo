def main():
    # Step 1: Get input from the user
    first_set = input()
    second_set = input()

    # Step 2: Split the inputs into separate values
    first_values = first_set.split()
    second_values = second_set.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0 

    # Step 4: Compare the corresponding values from both sets
    for index in range(3):  # Assuming we compare exactly three values as per the original pseudocode
        value_a = int(first_values[index])  # Convert to integer for comparison
        value_b = int(second_values[index])

        # If values are different, increment the difference counter
        if value_a != value_b:
            difference_count += 1 
    
    # Step 5: Evaluate the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point for the program execution
main()
