def main():
    # Step 1: Read input
    filePath = input()

    # Step 2: Normalize the file path
    normalizedPath = normalize(filePath)

    # Step 3: Output the result
    print(normalizedPath)

def normalize(filePath):
    # Remove additional leading slashes
    if filePath.startswith('//'):
        return '/' + filePath.lstrip('/')
    else:
        return filePath.lstrip('/')

# Entry point of the program
if __name__ == "__main__":
    main()
