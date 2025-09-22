def main():
    # Step 1: Accept two lines of input from the user
    first_input = input()
    second_input = input()
    
    # Step 2: Split the input strings into lists of numbers
    first_list = first_input.split()
    second_list = second_input.split()

    # Step 3: Initialize a counter to track differences
    difference_count = 0 
    
    # Step 4: Compare the numbers at corresponding positions
    for index in range(3):  # We are assumed to compare exactly 3 numbers
        first_number = int(first_list[index])  # Convert string to integer
        second_number = int(second_list[index])  # Convert string to integer
        
        # Step 5: Check if the numbers are different
        if first_number != second_number:
            difference_count += 1
            
    # Step 6: Assess the number of differences
    if difference_count < 3:
        print("YES")  # Less than three differences found
    else:
        print("NO")   # Three or more differences found

# Step 7: Execute main function if this script is run directly
if __name__ == "__main__":
    main()
