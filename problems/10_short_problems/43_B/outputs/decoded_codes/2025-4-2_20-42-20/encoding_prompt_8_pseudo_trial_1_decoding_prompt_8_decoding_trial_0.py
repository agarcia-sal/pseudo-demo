def main():
    firstString = input()
    secondString = input()
    
    cleanedFirstString = ''.join(c for c in firstString if c != ' ')
    cleanedSecondString = ''.join(c for c in secondString if c != ' ')
    
    characterFrequency = [0] * 52

    for char in cleanedFirstString:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
        else:
            index = ord(char) - ord('a') + 26
        characterFrequency[index] += 1

    for char in cleanedSecondString:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
        else:
            index = ord(char) - ord('a') + 26
        characterFrequency[index] -= 1

    isSufficient = True
    for count in characterFrequency:
        if count < 0:
            isSufficient = False
            break

    if isSufficient:
        print("YES")
    else:
        print("NO")

# To run the main function
if __name__ == "__main__":
    main()
