def doMain():
    # Step 2: Read two strings from user input
    first_input = input()
    second_input = input()
    
    # Step 3: Split the first_input into a list of strings
    first_list = first_input.split()
    # Step 4: Split the second_input into a list of strings
    second_list = second_input.split()
    
    # Step 5: Initialize a variable to count the differences
    differences_count = 0
    
    # Step 6: Check values in both lists for differences
    for index in range(3):  # Loop from 0 to 2 (inclusive)
        # Convert the values to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Compare the values and increment differences_count if they are not equal
        if first_value != second_value:
            differences_count += 1
    
    # Step 7: Determine the output based on the differences_count
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Call the doMain function if the script is executed directly
if __name__ == "__main__":
    doMain()
