class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = Counter(s)
        for i in t:
            if i not in counter or counter[i] != t.count(i):
                return False

        return True