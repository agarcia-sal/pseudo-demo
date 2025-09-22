def doMain():
    # Read two strings representing scores
    firstScoreString = input()
    secondScoreString = input()
    
    # Split the input strings into lists of scores
    firstScores = firstScoreString.split()
    secondScores = secondScoreString.split()
    
    # Initialize a counter for score differences
    scoreDifferenceCount = 0 
    
    # Iterate over the first three scores
    for index in range(3):
        # Convert string scores to integers
        firstScore = int(firstScores[index])
        secondScore = int(secondScores[index])
        
        # Check if the scores are different
        if firstScore != secondScore:
            # Increment the difference counter
            scoreDifferenceCount += 1 
    
    # Determine if the number of differences is less than 3
    if scoreDifferenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
doMain()
