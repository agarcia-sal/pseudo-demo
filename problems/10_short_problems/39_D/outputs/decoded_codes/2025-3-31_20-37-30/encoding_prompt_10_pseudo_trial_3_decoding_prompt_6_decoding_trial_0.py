def do_main():
    # Step 1: Input two strings
    t1 = input()
    t2 = input()
    
    # Step 2: Split the strings into lists of substrings
    tt1 = t1.split()  # Split t1 by whitespace
    tt2 = t2.split()  # Split t2 by whitespace
    
    # Step 3: Initialize counter for differences
    differences_count = 0 
    
    # Step 4: Compare the first three elements of both lists
    for index in range(3):  # Loop through first three elements
        # Convert string elements to integers
        a = int(tt1[index])  # Convert to integer
        b = int(tt2[index])  # Convert to integer
        
        # Step 5: Check for differences
        if a != b:  # If a is not equal to b
            differences_count += 1  # Increment the differences counter
            
    # Step 6: Determine the final result 
    if differences_count < 3:  # If differences are less than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO
        
# Step 7: Main execution block
if __name__ == "__main__":
    do_main()  # Call the main function
