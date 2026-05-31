class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        output = []
        for s in strs:          
            key = "".join(sorted(s))
            counts[key] = counts.get(key) or []
            counts[key].append(s)
            
        for x in counts.values():
            output.append(x)

        return output
    