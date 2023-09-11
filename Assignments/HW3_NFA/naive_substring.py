def naive_substring_search(pattern, s):
    """
    Implement the naive O(len(pattern) * len(s)) algorithm for finding
    all instances of pattern in s

    Parameters
    ----------
    pattern: string
        Search pattern
    s: string
        String in which to search for pattern
    
    Returns
    -------
    list of int:
        A list of all of the indices at which pattern exists in s
    """
    instances = []
    for i in range(len(s)-len(pattern)+1):
        j = 0
        valid = True
        while valid and j < len(pattern):
            if pattern[j] == s[i+j]:
                j += 1 # Continue along as long as we do match
            else:
                valid = False # Break out early as soon as we don't match
        if valid:
            instances.append(i)
    return instances

