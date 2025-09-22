def main():
    # Read input values from user
    t1 = input()  # First set of numbers as a string
    t2 = input()  # Second set of numbers as a string
    
    # Split input strings into lists of strings
    tt1 = t1.split()  # Splitting first input into words
    tt2 = t2.split()  # Splitting second input into words
    
    # Initialize a count of differences
    difference_count = 0 
    
    # Compare corresponding elements of the two lists
    for i in range(3):  # Loop through the first three elements
        a = int(tt1[i])  # Convert the i-th element of tt1 to an integer
        b = int(tt2[i])  # Convert the i-th element of tt2 to an integer
        
        if a != b:  # Check if the two numbers are not equal
            difference_count += 1  # Increment the difference count if they are not equal
    
    # Determine if the differences are fewer than 3
    if difference_count < 3:
        print("YES")  # Print "YES" if differences are fewer than 3
    else:
        print("NO")   # Print "NO" if differences are 3 or more

# Execute the main function
if __name__ == "__main__":
    main()  # Call the main function to run the code
