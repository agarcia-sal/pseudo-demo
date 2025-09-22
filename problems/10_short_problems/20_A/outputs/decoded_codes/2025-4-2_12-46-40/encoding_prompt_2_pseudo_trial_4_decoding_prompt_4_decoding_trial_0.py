import os
import re

def main():
    # Step 1: Read Input
    inputPath = input().strip()  # Get the input and strip leading/trailing whitespace
    
    # Step 2: Normalize Path
    normalizedPath = os.path.normpath(inputPath)  # Normalize the path
    
    # Step 3: Remove Leading Slashes
    # Replace multiple leading slashes with a single slash
    modifiedPath = re.sub(r'^/+', '/', normalizedPath)
    
    # Step 4: Output Result
    print(modifiedPath)  # Display the modified path

# Run the main function
if __name__ == "__main__":
    main()
