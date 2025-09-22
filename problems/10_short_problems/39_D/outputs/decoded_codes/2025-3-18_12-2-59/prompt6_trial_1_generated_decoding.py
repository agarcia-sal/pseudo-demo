def main():
    # Step 1: Get two lines of input from the user
    first_line = input()
    second_line = input()
    
    # Step 2: Split the input lines into individual elements
    first_list = first_line.split()
    second_list = second_line.split()
    
    # Step 3: Initialize a counter for differences
    difference_count = 0 
    
    # Step 4: Compare the first three elements from both lists
    for index in range(3):  # Loop through indices 0, 1, and 2
        # Convert the elements from strings to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Step 5: Count the number of differences
        if first_value != second_value:
            difference_count += 1  # Increment counter if values differ
    
    # Step 6: Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")  # Output "YES" if fewer than 3 differences
    else:
        print("NO")  # Output "NO" otherwise

# Step 7: Run the main function if this file is executed
if __name__ == "__main__":
    main()
