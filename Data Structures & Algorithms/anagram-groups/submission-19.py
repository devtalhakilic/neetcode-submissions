class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Output = {}
        for i in range(len(strs)):
            word1 = "".join(sorted(strs[i]))
            if word1 not in Output:
                Output[word1] = []
            Output[word1].append(strs[i])
        return list(Output.values())

