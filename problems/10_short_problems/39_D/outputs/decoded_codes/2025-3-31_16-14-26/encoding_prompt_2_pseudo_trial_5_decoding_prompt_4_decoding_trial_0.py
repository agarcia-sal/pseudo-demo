def main():
    # Step 2: Read input from the user
    inputString1 = input()
    inputString2 = input()
    
    # Step 4: Split the input strings into lists of tokens
    tokens1 = inputString1.split()
    tokens2 = inputString2.split()
    
    # Step 6: Initialize the difference counter
    differenceCount = 0
    
    # Step 7: Compare the first three entries of both lists
    for i in range(3):
        valueFromFirstInput = int(tokens1[i])
        valueFromSecondInput = int(tokens2[i])
        
        # Compare values and increment the counter if they are different
        if valueFromFirstInput != valueFromSecondInput:
            differenceCount += 1
            
    # Step 8 and 9: Output results based on the difference count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    main()
