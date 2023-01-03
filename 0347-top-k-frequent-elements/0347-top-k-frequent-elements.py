class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for num in range(len(nums)+1)]
        
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n,c in count.items():
            freq[c].append(n)
        
        res=[]
        for j in range(len(freq)-1,0,-1):
            for n in freq[j]:
                res.append(n)
                if len(res) == k:
                    return res