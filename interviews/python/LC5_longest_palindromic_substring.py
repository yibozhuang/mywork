def longestPalindrome(s):
    str_len = len(s)
    if str_len == 0:
        return ""

    # Initialize DP table (dimensions: str_len x str_len)
    memo = [[0 for i in range(str_len)] for j in range(str_len)]

    start = 0 # Starting index of the longest palindrome
    max_len = 1 # Length of the longest palindrome

    # Fill DP table for single char palindromes
    for i in range(str_len):
        memo[i][i] = True

    # Fill DP table for 2 char long palindromes
    for i in range(str_len - 1):
        j = i + 1
        if s[i] == s[j]:
            memo[i][j] = True
            start = i
            max_len = 2
        else:
            memo[i][j] = False

    # Fill DP table for palindromes of every other length starting from 3
    length = 3
    while length <= str_len:
        for i in range(str_len - 2):
            j = i + (length - 1)
            if j < str_len: # if calculated j is a valid value
                if s[i] == s[j] and memo[i+1][j-1]:
                    memo[i][j] = True
                    start = i
                    max_len = length
                else:
                     memo[i][j] = False
        length += 1

    solution = s[start: start + max_len]
    return solution

print(longestPalindrome("babad"))
