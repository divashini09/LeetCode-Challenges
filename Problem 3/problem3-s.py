class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Initialize a DP table with False values
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: empty pattern matches empty string
        dp[0][0] = True

        # Fill first row where s is empty, handling cases with '*' in the pattern
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Populate the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # If current characters match, or pattern has '.', carry over the result
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                
                # If pattern contains '*', handle zero or more occurrences of previous element
                elif p[j - 1] == '*':
                    # Check zero occurrence of the element before '*'
                    dp[i][j] = dp[i][j - 2]
                    
                    # Check if the character preceding '*' matches current character in s
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        # The result for matching the entire s and p is in the bottom-right corner of the DP table
        return dp[len(s)][len(p)]
