class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3 = []
        for value in nums1:
            num3.append(value)
        for value in nums2:
            num3.append(value)
        num3.sort()
        if len(num3) % 2 != 0:
            index = int(round(len(num3)/2))
            return num3[index]
        else:
            
           
            
            return ((num3[(len(num3)//2-1)] + num3[(len(num3)//2)])/2.0)