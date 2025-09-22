def normalizeFilePath():
    # Step 1: Read the input
    inputPath = input()
    
    # Step 2: Remove leading and trailing whitespace
    trimmedPath = inputPath.strip()
    
    # Step 3: Normalize the file path
    normalizedPath = trimmedPath.replace("\\", "/")  # normalizing backslashes to forward slashes
    normalizedPath = normalizedPath.replace("//", "/")  # reducing multiple slashes

    # This loop handles multiple leading slashes
    while normalizedPath.startswith("//"):
        normalizedPath = normalizedPath[1:]  # keep removing leading slash
    
    # Step 4: Ensure only one leading slash
    if not normalizedPath.startswith("/"):
        finalPath = "/" + normalizedPath
    else:
        finalPath = normalizedPath

    # Step 5: Output the final modified file path
    print(finalPath)
