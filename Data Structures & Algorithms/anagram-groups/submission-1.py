class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for s in strs:          
            key = "".join(sorted(s))
            counts[key] = counts.get(key) or []
            counts[key].append(s)
        return list(counts.values())
    