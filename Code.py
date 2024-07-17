class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s1 = list(s)
        i = 0
        while(i<(len(s1)-i-1)):
            if s1[i] == s1[len(s1)-i-1]:
                i += 1
                continue
            if s1[i] < s1[len(s1)-i-1]:
                s1[len(s1)-i-1] = s1[i]
            else:
                s1[i] = s1[len(s1)-i-1]
            i += 1
        return "".join(s1)
