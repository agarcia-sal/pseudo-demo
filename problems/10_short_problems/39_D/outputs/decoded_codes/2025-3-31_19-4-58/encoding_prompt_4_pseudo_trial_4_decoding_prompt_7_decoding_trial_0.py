def main():
    # Read input values
    t1 = input()  # First string input
    t2 = input()  # Second string input

    # Split the input strings into lists
    tt1 = t1.split()  # Split the first input string into a list of words
    tt2 = t2.split()  # Split the second input string into a list of words
    
    # Initialize the result counter for differences
    differenceCount = 0 

    # Compare the first three elements of both lists
    for index in range(3):  # Looping through first 3 indices (0 to 2)
        a = int(tt1[index])  # Convert list element to integer from the first list
        b = int(tt2[index])  # Convert list element to integer from the second list
        if a != b:  # Check if values are different
            differenceCount += 1  # Increment the difference counter

    # Check if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences

# Execute the main function when the script runs
if __name__ == "__main__":
    main()
