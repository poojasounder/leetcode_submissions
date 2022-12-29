class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {} # []letters -> the actual string
        for string in strs:
            sortS = ''.join(sorted(string)) 
            hashmap[sortS] = hashmap.get(sortS,[])
            if sortS in hashmap:
                hashmap[sortS].append(string)
        return hashmap.values()
            