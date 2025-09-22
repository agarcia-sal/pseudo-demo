def doMain():
    # Step 2: Read the first line of input
    input_string1 = input()
    # Step 3: Read the second line of input
    input_string2 = input()
    
    # Step 4: Split the input strings into lists of strings
    number_list1 = input_string1.split()
    number_list2 = input_string2.split()
    
    # Step 6: Initialize a counter for differences
    difference_count = 0
    
    # Step 7: Compare the values at each index
    for i in range(3):  # Loop from index 0 to 2 (inclusive)
        # Convert the elements to integers
        value_a = int(number_list1[i])
        value_b = int(number_list2[i])
        
        # Step 7c: Check for differences
        if value_a != value_b:
            difference_count += 1  # Increment the difference count if values are not equal
    
    # Step 8: Determine output based on the difference count
    if difference_count < 3:
        print("YES")  # Output "YES" if there are less than 3 differences
    else:
        print("NO")   # Output "NO" if 3 or more differences exist

# Step 10: Execute the main function if the script is run directly
if __name__ == "__main__":
    doMain()
