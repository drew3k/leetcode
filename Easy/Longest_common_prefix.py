class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = copy.deepcopy(strs)

        def s(lst):
            lst2 = sorted(lst, key=len)
            return lst2

        prefix = s(prefix)[0]
        for word in strs:
            for i in range(len(prefix)):
                if word[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
        return prefix