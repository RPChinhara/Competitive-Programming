# Given two strings, find the length of longest subsequence present in both of them. Both the strings are in uppercase Latin alphabets.

def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D table to store the lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table using bottom-up dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Example Usage:
str1 = "ABCDGH"
str2 = "AEDFHR"
result = longest_common_subsequence(str1, str2)

print(f"The length of the Longest Common Subsequence is: {result}")
