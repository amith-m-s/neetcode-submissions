from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g=defaultdict(list)
        for i in strs:
            freq=[0]*26
            for j in i:
                freq[ord(j) - ord('a')] += 1
            g[tuple(freq)].append(i)
        return list(g.values())