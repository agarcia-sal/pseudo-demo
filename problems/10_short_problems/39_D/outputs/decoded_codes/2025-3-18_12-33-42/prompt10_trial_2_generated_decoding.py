def do_main():
    # Step 1: Input the values for two test cases
    t1 = input()
    t2 = input()
    
    # Step 2: Split the input strings into lists of string elements
    tt1 = t1.split()  # Converts the input string to a list of words
    tt2 = t2.split()  # Converts the input string to a list of words
    
    # Step 3: Initialize a counter for differences
    difference_count = 0
    
    # Step 4: Compare the elements of the two lists
    for index in range(3):  # Assuming the lists have exactly three elements
        a = int(tt1[index])  # Convert string to integer
        b = int(tt2[index])  # Convert string to integer
        
        # Step 5: Count the differences between the two lists
        if a != b:
            difference_count += 1
    
    # Step 6: Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution point
if __name__ == "__main__":
    do_main()
