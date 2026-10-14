class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for word in strs:
            count = [0] * 26
            
            for c in word:
                count[ord(c) - ord("a")] += 1

            anagramMap[tuple(count)].append(word)

        return list(anagramMap.values())