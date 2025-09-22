def normalize_path():
    # Step 2: Read Input
    inputPath = input()
    
    # Step 3: Clean the Input Path
    # Normalize the inputPath by removing redundant slashes
    normalizedPath = '/'.join(part for part in inputPath.split('/') if part)

    # Step 4: Substitute Leading Slashes
    # Replace leading slashes with a single leading slash
    finalPath = '/' + normalizedPath if normalizedPath else '/'

    # Step 5: Output the Result
    print(finalPath)

# Step 1: Define Main Procedure
if __name__ == "__main__":
    normalize_path()
