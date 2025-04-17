# Write your solution here
def longestPalindrome(s):
    if not s:
        return ""
    
    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""

    for i in range(len(s)):
        # odd-length palindromes
        temp1 = expandAroundCenter(i, i)

        #Even-length palindromes
        temp2 = expandAroundCenter(i, i+1)

        #Update longest if necessary
        if len(temp1) > len(longest):
            longest = temp1
        if len(temp2) > len(longest):
            longest = temp2

    return longest
