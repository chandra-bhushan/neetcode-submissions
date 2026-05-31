class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for s in strs:          
            key = "".join(sorted(s))
            counts[key].append(s)
        return list(counts.values())
    