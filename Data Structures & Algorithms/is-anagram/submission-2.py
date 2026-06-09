class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        one = []
        two = []
        for i in range(len(s)):
            one.append(s[i])
        for i in range(len(t)):
            two.append(t[i])
        
        one.sort()
        two.sort()

        for i in range(len(one)):
            if one[i] != two[i]:
                return False

        return True