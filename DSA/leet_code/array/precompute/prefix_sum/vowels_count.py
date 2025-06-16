"""You are given a 0-indexed array of strings words and a 2D array of integers queries.
Each query queries[i] = [li, ri] asks us to find the number of strings present at the indices ranging from li to ri (both inclusive) of words that start and end with a vowel.
Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

Idea : prefix_sum to get nb of v_words observed before index (add 0 at beginning) then match query indexes with prefix_sum indexes (cf inclusivity) 
for instance calculus of nb of v_words in between.

"""
from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(('a','e','i','o','u'))

        n = len(words)
        prefix_sum = [0] * (n+1)
        s = 0
        for i,elt in enumerate(words,start=1):
            if elt[0] in vowels and elt[-1] in vowels:
                s += 1
            prefix_sum[i] = s
        
        ans = [0] * len(queries)
        for i,q in enumerate(queries):
            ans[i] = prefix_sum[q[1]+1] - prefix_sum[q[0]]
        return ans
