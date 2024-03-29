def groupAnagrams(strs: list[str]) -> list[list[str]]:
    from collections import defaultdict

    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    return ans.values()

    
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

"""
    res = defaultdict(list)
    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)

    return res.values()
"""