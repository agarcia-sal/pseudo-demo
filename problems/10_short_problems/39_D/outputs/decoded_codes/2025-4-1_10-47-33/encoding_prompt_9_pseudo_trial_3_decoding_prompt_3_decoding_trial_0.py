def main():
    # Step 1: Read the first set of integers from the user
    print("Enter the first set of three integers:")
    first_set = input()
    
    # Step 2: Read the second set of integers from the user
    print("Enter the second set of three integers:")
    second_set = input()
    
    # Step 3: Split the input strings into lists of integers
    first_list = first_set.split()
    second_list = second_set.split()
    
    # Step 4: Initialize a counter for differences
    difference_count = 0
    
    # Step 5: Compare the corresponding integers from both lists
    for index in range(3):
        # Convert string to integer for comparison
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Check if the numbers are different
        if first_number != second_number:
            difference_count += 1
            
    # Step 6: Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")
        
# This block ensures that the main function is only called when this script is run directly
if __name__ == "__main__":
    main()
