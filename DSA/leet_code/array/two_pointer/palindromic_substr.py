"""
Given a string s, return number of palindromes within it
Idea : palindrome can be easily built from another one

1) Each letter is a center
2) Treat the special case where multiple same letters repeat (2 out of n palindromes) iterating on the right
3) From the original same letter palindrome, check if new palindroms
"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, n, i = 0, len(s), 0
        while i < n:
            j, k = i-1,i
            while k < n-1 and s[k] == s[k+1]:
                k+=1
            ans += (k-j) * (k-j+1) / 2
            i = k = k+1
            while j >= 0 and k < n and s[j] == s[k]:
                j, k, ans = j-1, k+1, ans+1
        return ans