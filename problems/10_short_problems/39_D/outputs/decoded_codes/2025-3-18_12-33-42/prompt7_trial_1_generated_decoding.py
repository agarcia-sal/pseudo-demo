def main():
    # Prompt the user to input the first string of integers
    t1 = input()
    
    # Prompt the user to input the second string of integers
    t2 = input()
    
    # Split the input strings by spaces to create lists of integers
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a counter for mismatches
    mismatchCount = 0
    
    # Check for exactly three integers as expected
    if len(tt1) != 3 or len(tt2) != 3:
        print("Input must contain exactly three integers.")
        return
    
    # Iterate over the range of 3 to compare the corresponding integers
    for index in range(3):
        # Convert the string representations to integers
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Increment the mismatch counter if the integers are not equal
        if a != b:
            mismatchCount += 1
            
    # Print "YES" if there are fewer than 3 mismatches, otherwise print "NO"
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
