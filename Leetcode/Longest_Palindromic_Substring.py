class Solution:
    def longestPalindrome(self, s: str) -> str:
        result_len = 0
        result = ''

        for i in range(len(s)):
            # for odd
            l,r = i,i


            while l >= 0 and r<len(s) and s[l] == s[r]:
                if result_len < (r-l+1):
                    result = s[l:r+1]
                    result_len = (r-l+1)
                l -= 1
                r += 1

            # For even
            l,r = i,i+1
            while l >= 0 and r<len(s) and s[l] == s[r]:
                if result_len < (r-l+1):
                    result = s[l:r+1]
                    result_len = (r-l+1)
                l -= 1
                r += 1
            
        return result