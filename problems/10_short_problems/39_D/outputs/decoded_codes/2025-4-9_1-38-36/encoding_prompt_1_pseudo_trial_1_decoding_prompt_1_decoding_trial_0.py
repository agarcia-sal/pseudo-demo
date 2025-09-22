def main():
    # Step 1: Accept input values from the user
    first_input = input()
    second_input = input()
    
    # Step 2: Split the input strings into lists of integers
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Step 3: Initialize a counter for differences
    difference_count = 0
    
    # Step 4: Compare corresponding integers in both lists
    for index in range(3):  # Loop from 0 to 2 (inclusive)
        # Convert the values from strings to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Step 5: Check if the two values are different
        if first_value != second_value:
            difference_count += 1
            
    # Step 6: Evaluate the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Run the main function when the program starts
main()
